"""Phase 3.6 prospective pilot schema boundary and no-false-evidence checks."""

import copy
import unittest

from research.phase3_6.annotation_protocol import SLOTS, compare_pair, verify


def fixture():
    return {
        "protocol": "P36-S0-PILOT-V1",
        "case_id": "P36-20261114-0900-PHT",
        "capture": {
            "instrument": "BINANCE:PAXGUSDT", "market_type": "SPOT",
            "candle_kind": "STANDARD", "timeframe": "5m",
            "source_mode": "LIVE_CHART",
            "target_cutoff_utc": "2026-11-14T01:00:00Z",
            "last_visible_closed_utc": "2026-11-14T01:00:00Z",
            "captured_at_utc": "2026-11-14T01:01:00Z",
            "future_hidden": True,
            "snapshot_sha256": "a" * 64,
        },
        "annotation": {
            "reviewer_id": "R1", "recorded_at_utc": "2026-11-14T01:02:00Z",
            "blind_to_peer": True, "selection": "ANCHOR",
            "regime": "UP", "swing_side": "HIGH",
            "pivot_origin_utc": "2026-11-14T00:45:00Z",
            "level_quote": "3900.25", "role": "HH",
            "scale": "5M_STRUCTURAL", "reason": "Constructed test fixture, not a real annotation",
        },
    }


class PilotProtocolTests(unittest.TestCase):
    def test_locked_sampling_grid_has_twelve_distinct_future_slots(self):
        self.assertEqual(len(SLOTS), 12)
        self.assertEqual(len(set(SLOTS.values())), 12)
        self.assertEqual(sorted(SLOTS)[0], "P36-20261114-0900-PHT")
        self.assertEqual(sorted(SLOTS)[-1], "P36-20261117-2100-PHT")

    def test_valid_constructed_live_record_is_not_authenticated(self):
        self.assertEqual(verify(fixture()), "REPORTED_LIVE_TIMELINESS_NOT_AUTHENTICATED")

    def test_abstain_retains_uncertainty(self):
        obj = fixture()
        obj["annotation"].update(selection="ABSTAIN", regime="UNKNOWN", swing_side=None,
                                 pivot_origin_utc=None, level_quote=None, role=None,
                                 reason="Cannot identify a structural reference")
        self.assertEqual(verify(obj), "REPORTED_LIVE_TIMELINESS_NOT_AUTHENTICATED")

    def test_wrong_market_and_future_visibility_rejected(self):
        for field, value in (("instrument", "BINANCE:XAUTUSDT"), ("market_type", "PERP"),
                             ("candle_kind", "HEIKIN_ASHI"), ("future_hidden", False)):
            obj = fixture()
            obj["capture"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                verify(obj)

    def test_late_live_declaration_is_invalid(self):
        for stamp in ("2026-11-14T01:05:00Z", "2026-11-14T02:00:00Z"):
            obj = fixture()
            obj["annotation"]["recorded_at_utc"] = stamp
            with self.subTest(stamp=stamp), self.assertRaises(ValueError):
                verify(obj)

    def test_bad_observation_clock_and_wrong_cutoff_rejected(self):
        for field, value in (("captured_at_utc", "2026-11-14T00:59:00Z"),
                             ("last_visible_closed_utc", "2026-11-14T00:55:00Z"),
                             ("target_cutoff_utc", "2026-11-14T00:55:00Z"),
                             ("snapshot_sha256", "no-digest")):
            obj = fixture()
            obj["capture"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                verify(obj)

    def test_incoherent_structural_role_rejected(self):
        for regime, side, role in (("DOWN", "HIGH", "HH"), ("UP", "LOW", "HH"),
                                   ("UP", "HIGH", "LH")):
            obj = fixture()
            obj["annotation"].update(regime=regime, swing_side=side, role=role)
            with self.subTest(role=role, side=side, regime=regime), self.assertRaises(ValueError):
                verify(obj)

    def test_uncertain_anchor_may_have_no_role(self):
        obj = fixture()
        obj["annotation"].update(regime="UNKNOWN", role=None)
        self.assertEqual(verify(obj), "REPORTED_LIVE_TIMELINESS_NOT_AUTHENTICATED")

    def test_invalid_price_origin_and_missing_reason_rejected(self):
        for field, value in (("level_quote", "0"), ("level_quote", "-1"), ("level_quote", "NaN"),
                             ("pivot_origin_utc", "2026-11-14T01:00:00Z"), ("reason", "")):
            obj = fixture()
            obj["annotation"][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                verify(obj)

    def test_frozen_prefix_is_practice_not_prospective(self):
        obj = fixture()
        obj["capture"]["source_mode"] = "FROZEN_PREFIX_PRACTICE"
        obj["annotation"]["recorded_at_utc"] = "2026-11-14T03:00:00Z"
        self.assertEqual(verify(obj), "FROZEN_PREFIX_PRACTICE_ONLY")

    def test_pair_uses_same_capture_and_distinct_reviewers(self):
        one, two = fixture(), fixture()
        two["annotation"]["reviewer_id"] = "R2"
        self.assertEqual(compare_pair(one, two)["exact_reference"], True)
        two["annotation"]["pivot_origin_utc"] = "2026-11-14T00:40:00Z"
        self.assertEqual(compare_pair(one, two)["exact_reference"], False)
        two["capture"]["snapshot_sha256"] = "b" * 64
        with self.assertRaises(ValueError):
            compare_pair(one, two)

    def test_pair_cannot_silently_conflate_practice_or_abstention(self):
        one, two = fixture(), fixture()
        two["annotation"]["reviewer_id"] = "R2"
        two["annotation"].update(selection="ABSTAIN", swing_side=None, pivot_origin_utc=None,
                                 level_quote=None, role=None, reason="Ambiguous")
        self.assertIsNone(compare_pair(one, two)["exact_reference"])
        two["capture"]["source_mode"] = "FROZEN_PREFIX_PRACTICE"
        with self.assertRaises(ValueError):
            compare_pair(one, two)


if __name__ == "__main__":
    unittest.main()
