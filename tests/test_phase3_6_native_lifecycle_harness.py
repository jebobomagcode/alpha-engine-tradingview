"""Guard the provenance and read-only instrumentation of the temporary Pine audit."""

from hashlib import sha256
import subprocess
import unittest

from research.phase3_6 import native_v015_lifecycle_audit as audit


class NativeLifecycleHarness(unittest.TestCase):
    def test_exact_source_and_instrumentation_only(self):
        release = subprocess.check_output(["git", "show", f"{audit.SOURCE_COMMIT}:{audit.SOURCE_PATH}"])
        self.assertEqual(sha256(release).hexdigest(), audit.SOURCE_SHA256)
        source = audit.generate(release)
        self.assertEqual(source.count(audit.DECLARATIONS), 1)
        self.assertEqual(source.count(audit.OBSERVATIONS), 1)
        self.assertEqual(source.count(audit.PANEL), 1)
        self.assertLess(source.index("    bool reaction ="), source.index(audit.OBSERVATIONS))
        self.assertLess(source.index(audit.OBSERVATIONS), source.index("    aiUpper := nextHigh"))
        restored = source.removesuffix(audit.PANEL).replace(audit.OBSERVATIONS, "").replace(audit.DECLARATIONS, "")
        restored = restored.replace("Alpha Engine | v0.1.5 Lifecycle Audit", "Alpha Engine | Integrated Research v0.1.5")
        restored = restored.replace('input.string("R1-B", "Reference policy"', 'input.string("R1-A", "Reference policy"')
        self.assertEqual(restored.encode(), release)

    def test_rejects_unpinned_source(self):
        with self.assertRaisesRegex(ValueError, "exact accepted"):
            audit.generate(b"// Pine source is not pinned")
