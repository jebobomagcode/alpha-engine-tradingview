"""Adjudicated boundary cases and bounded whole-engine reference search."""

from dataclasses import replace
from inspect import getsource
from itertools import product
from pathlib import Path
from random import Random
import unittest

from research.phase3_6 import pine_lifecycle_projection as projection
from research.phase3_6.ai_structure_candidate import replay_structure
from research.phase3_6.lifecycle_parity_oracle import Candle, Episode, Zone
from research.phase3_6.reference_model import Bar
from test_phase3_6_integrated_replay import frozen_tape


def tape(closes):
    return tuple(Bar(i * 5, p, p + 1, p - 1, p) for i, p in enumerate(closes))


class LifecycleAuditTests(unittest.TestCase):
    def test_terminal_origins_and_reference_candidates_advance_per_side(self):
        # Enumerate every nine-bar sequence over three prices, plus longer
        # deterministic paths that can complete several structural regimes.
        random = Random(30615)
        exhaustive = (tape(prices) for prices in product((95, 100, 105), repeat=9))
        longer = [tape(tuple(random.randrange(90, 111) for _ in range(72))) for _ in range(96)]
        longer += [frozen_tape(), frozen_tape()[:100] + frozen_tape()[101:]]
        seen_events = 0
        sequences = 0
        for bars in exhaustive:
            self.check_origins(replay_structure(bars, as_of=45, left=1, right=1))
            sequences += 1
        self.assertEqual(sequences, 19_683)
        for bars in longer:
            for width in (1, 2, 3, 4):
                for policy in ("A", "B"):
                    frames = replay_structure(bars, as_of=bars[-1].cutoff, policy=policy,
                                              left=width, right=width)
                    seen_events += self.check_origins(frames)
        self.assertGreater(seen_events, 100)

    def check_origins(self, frames):
        latest = {}
        terminal = set()
        total = 0
        for frame in frames:
            for event in frame.events:
                ref = event.reference
                identity = ref.side, ref.origin_open
                self.assertNotIn(identity, terminal)
                terminal.add(identity)
                self.assertGreaterEqual(event.cutoff, ref.earliest_cross_close)
                total += 1
            for ref in frame.structure.references:
                self.assertGreaterEqual(ref.origin_open, latest.get(ref.side, -1))
                latest[ref.side] = ref.origin_open
            for item in frame.references:
                ref = item.reference
                if (ref.side, ref.origin_open) in terminal:
                    self.assertEqual(item.status, "CONSUMED")
        return total

    def test_long_history_has_no_repeated_terminal_events(self):
        bars = []
        frozen = frozen_tape()
        for i in range(8):
            bars.extend(replace(bar, start=bar.start + 1440 * i) for bar in frozen)
        frames = replay_structure(bars, as_of=bars[-1].cutoff)
        self.assertEqual(len(frames), 2304)
        self.assertGreater(self.check_origins(frames), 20)

    def test_mutations_disagree_with_independent_expected_outcomes(self):
        block = Zone("X", "BLOCK", 1, 97, 102, 5)
        wick_touch = Candle(5, 98, 101, 94, 96)
        invalid_episode = Episode("A", touched=True, ended=True)
        episode_args = dict(previous=invalid_episode, candle=Candle(5, 100, 99, 101, 98),
                            predecessor=None, adjacent=True, context_ok=True, bullish_context=True,
                            armed_anchor="A", support_low=97, support_high=102)
        ref = projection.PineReference(10, 30, 100, "HH", "ARMED")
        args = dict(reference=ref, above=True, previous_close=100, current_close=101, opened=25)
        tests = (
            (projection.project_zone, 'if invalidated:', 'if invalidated and False:',
             lambda f: f(block, wick_touch).state, "INVALIDATED"),
            (projection.project_zone, 'candle.opened < zone.known_at', 'candle.opened <= zone.known_at',
             lambda f: f(block, Candle(5, 100, 103, 99, 101)).state, "GEOMETRIC TEST"),
            (projection.project_episode, 'EpisodeDecision(Episode(),', 'EpisodeDecision(previous,',
             lambda f: f(**episode_args).state, Episode()),
            (projection.project_cross, 'reference.armed_at > opened', 'False',
             lambda f: f(**args), False),
            (projection.project_cross, 'previous_close <= reference.level', 'previous_close < reference.level',
             lambda f: f(**(args | {"opened": 30})), True),
            (projection.project_episode, 'context_ok and bullish_context', 'bullish_context',
             lambda f: f(**(episode_args | {
                 "previous": Episode(), "context_ok": False, "candle": Candle(5, 99, 107, 98, 106),
                 "predecessor": Candle(0, 105, 106, 99, 100),
             })).reaction, False),
        )
        for original, old, new, evaluate, expected in tests:
            with self.subTest(function=original.__name__, condition=old):
                self.assertEqual(evaluate(original), expected)
                source = getsource(original)
                self.assertIn(old, source)
                namespace = vars(projection).copy()
                exec(compile(source.replace(old, new, 1), "<controlled mutation>", "exec"), namespace)
                self.assertNotEqual(evaluate(namespace[original.__name__]), expected)

    def test_candidate_guards_terminal_watermark_and_same_cutoff_consumption(self):
        source = (Path(__file__).resolve().parents[1] / "pine/alpha-engine-research.pine").read_text()
        self.assertIn('if not na(terminalOrigin) and origin < terminalOrigin', source)
        self.assertIn('ResearchReference.new(origin, na, level, role, "RETIRED")', source)
        self.assertIn('bool supportConsumed = supportKnown and crossLow', source)
        self.assertLess(source.index('if invalidSupport or departure or supportConsumed'),
                        source.index('bool reaction ='))
