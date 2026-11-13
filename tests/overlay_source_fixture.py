"""Undo display-only changes when checking the pinned research source."""

import re


def without_new_visuals(source: str) -> str:
    """Recover the v0.1.8 Pine body, keeping original calculation coverage."""
    source = without_observation_visuals(source).split("\n// Chart Fibonacci and EMA overlays.", 1)[0]
    source = source.replace("Integrated Research v0.1.9", "Integrated Research v0.1.8", 1)
    source = source.replace("max_labels_count = 37, max_lines_count = 5",
                            "max_labels_count = 37, max_lines_count = 2", 1)
    source = re.sub(r"AE-0\.1\.9-[0-9a-f]{12}", "AE-0.1.8-6927cc23e060", source, count=1)
    source = re.sub(r"\n// Numeric values and pivot identities[^\n]*\n(?:var [^\n]* aiFib[^\n]*\n){6}",
                    "\n", source, count=1)
    source = source.replace("    aiFib50 := na\n    aiFib618 := na\n    aiFib705 := na\n", "", 1)
    source = re.sub(
        r"(?m)^                aiFib50 := [^\n]+\n(?:                aiFib[^\n]*\n){5}"
        r"                aiFib := [^\n]+",
        '                aiFib := str.tostring(startFib + direction * distance * 0.5, format.mintick)'
        ' + " / " + str.tostring(startFib + direction * distance * 0.618, format.mintick)'
        ' + " / " + str.tostring(startFib + direction * distance * 0.705, format.mintick)',
        source, count=1,
    )
    return source


def without_observation_visuals(source: str) -> str:
    """Recover the guide increment before adding observation state taps."""
    source = source.split("\n// Chart contact, reaction and nominal geometry.", 1)[0]
    source = source.replace("Integrated Research v0.1.10", "Integrated Research v0.1.9", 1)
    source = source.replace("max_labels_count = 54, max_lines_count = 8",
                            "max_labels_count = 37, max_lines_count = 5", 1)
    source = re.sub(r"AE-0\.1\.10-[0-9a-f]{12}", "AE-0.1.9-98ca36885208", source, count=1)
    source = re.sub(r"\n// Close-stamped observations[^\n]*\n(?:var [^\n]* ai(?:Visual|Geometry)[^\n]*\n){7}",
                    "\n", source, count=1)
    source = re.sub(r"(?m)^    ai(?:Visual|Geometry(?:Entry|Stop|Target|R) := na)[^\n]*\n", "", source)
    source = re.sub(
        r"(?m)^            aiGeometryEntry := [^\n]+\n(?:            aiGeometry[^\n]*\n){3}"
        r"            aiGeometry := [^\n]+",
        '            aiGeometry := str.tostring(close, format.mintick) + " / "'
        ' + str.tostring(stopLevel, format.mintick) + " / " + str.tostring(targetLevel, format.mintick)'
        ' + " · " + str.tostring((targetLevel - close) / (close - stopLevel), "#.00") + "R"',
        source, count=1,
    )
    return source
