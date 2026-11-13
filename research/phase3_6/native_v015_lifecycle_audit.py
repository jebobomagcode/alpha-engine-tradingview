"""Generate an unsaved TradingView audit from the exact accepted v0.1.5 Pine source."""

import argparse
from hashlib import sha256
from pathlib import Path
import subprocess
import sys


SOURCE_COMMIT = "5a75f639a2216e769842b1e235783062fbe030d5"
SOURCE_PATH = "pine/alpha-engine-research.pine"
SOURCE_SHA256 = "f29e7980db347dd9cfd4e799a4c3b807ccf6ed2e5d05bc709281f96eacdaa452"

DECLARATIONS = """var int auditBars = 0
var int auditStart = na
var int auditBandCount = 0
var int auditResetCount = 0
var int auditRecrossCount = 0
var int auditHighReset = na
var int auditLowReset = na
var string auditBand = "—"
var string auditReset = "—"
var string auditRecross = "—"
var string auditRetired = "NOT RUN"

"""

OBSERVATIONS = """    auditBars += 1
    if na(auditStart)
        auditStart := time
    if supportConsumed and not invalidSupport
        auditBandCount += 1
        auditBand := utc(time_close) + " UTC · HL " + str.tostring(aiLower.level, format.mintick) + " / close " + str.tostring(close, format.mintick) + "\\n" + aiWorkflow + " · ended " + str.tostring(aiEpisodeEnded) + " / reaction " + str.tostring(reaction)

    if crossHigh and aiUpper.armedAt == auditHighReset or crossLow and aiLower.armedAt == auditLowReset
        ResearchReference recross = crossHigh ? aiUpper : aiLower
        auditRecrossCount += 1
        auditRecross := recross.role + " " + str.tostring(recross.level, format.mintick) + " · " + utc(recross.origin) + "\\n" + utc(recross.armedAt) + " → " + utc(time_close) + " UTC"
    if aiUpper.state == "RESET PENDING" and nextHigh.state == "ARMED" and aiUpper.origin == nextHigh.origin
        auditHighReset := time_close
        auditResetCount += 1
        auditReset := nextHigh.role + " " + str.tostring(nextHigh.level, format.mintick) + " · " + utc(nextHigh.origin) + " / " + utc(time_close) + " UTC"
    if aiLower.state == "RESET PENDING" and nextLow.state == "ARMED" and aiLower.origin == nextLow.origin
        auditLowReset := time_close
        auditResetCount += 1
        auditReset := nextLow.role + " " + str.tostring(nextLow.level, format.mintick) + " · " + utc(nextLow.origin) + " / " + utc(time_close) + " UTC"

    // These ordered origins are injected into the release helper. They are not market events.
    if auditBars == 1
        ResearchReference older = updateRef(ResearchReference.new(), 10, close, "HH", 20, "CONSUMED", true, true)
        ResearchReference equal = updateRef(ResearchReference.new(), 20, close, "HH", 20, "CONSUMED", true, true)
        ResearchReference newer = updateRef(ResearchReference.new(), 30, close, "HH", 20, "CONSUMED", true, true)
        auditRetired := older.state + " / " + equal.state + " / " + newer.state
"""

PANEL = """
var table auditPanel = table.new(position.middle_left, 2, 6, bgcolor = color.rgb(20, 26, 36), frame_color = color.rgb(55, 70, 91), frame_width = 1)
if barstate.islast and aiEnabled
    researchRow(auditPanel, 0, "v0.1.5 lifecycle audit", syminfo.tickerid + " · " + aiPolicy + " · " + str.tostring(aiZoneTicks) + " ticks")
    researchRow(auditPanel, 1, "Closed chart bars", str.tostring(auditBars) + " · " + utc(auditStart) + " → " + utc(aiDecisionAt) + " UTC")
    researchRow(auditPanel, 2, "Consumed in band · " + str.tostring(auditBandCount), auditBand)
    researchRow(auditPanel, 3, "Reset → armed · " + str.tostring(auditResetCount), auditReset)
    researchRow(auditPanel, 4, "Reset → re-cross · " + str.tostring(auditRecrossCount), auditRecross)
    researchRow(auditPanel, 5, "Injected watermark", auditRetired)
"""


def generate(source: bytes) -> str:
    if sha256(source).hexdigest() != SOURCE_SHA256:
        raise ValueError("Expected exact accepted v0.1.5 source")
    text = source.decode()
    text = text.replace("Alpha Engine | Integrated Research v0.1.5", "Alpha Engine | v0.1.5 Lifecycle Audit")
    text = text.replace('input.string("R1-A", "Reference policy"', 'input.string("R1-B", "Reference policy"')
    text = text.replace("if aiEnabled and chartOK and barstate.isconfirmed", DECLARATIONS + "if aiEnabled and chartOK and barstate.isconfirmed")
    text = text.replace("    aiUpper := nextHigh\n", OBSERVATIONS + "    aiUpper := nextHigh\n")
    return text + PANEL


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Optional exact accepted source file")
    args = parser.parse_args()
    source = args.source.read_bytes() if args.source else subprocess.check_output(
        ["git", "show", f"{SOURCE_COMMIT}:{SOURCE_PATH}"]
    )
    sys.stdout.write(generate(source))


if __name__ == "__main__":
    main()
