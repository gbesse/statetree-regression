import tempfile
import unittest
from pathlib import Path

from statetree_regression import compare, read_markers


class RegressionTests(unittest.TestCase):
    def test_detects_changed_outcome(self):
        old = {"patrol": [("Search", "Exit", "success")]}
        new = {"patrol": [("Search", "Exit", "failure")]}
        self.assertEqual(compare(old, new)[0]["scenario"], "patrol")

    def test_reads_prefixed_unreal_log(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "log.txt"
            path.write_text('LogTemp: Display: STREG {"scenario":"patrol","state":"Search","event":"Exit","outcome":"success"}\n')
            self.assertEqual(read_markers(path), {"patrol": [("Search", "Exit", "success")]})

    def test_rejects_missing_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "log.txt"
            path.write_text('STREG {"scenario":"patrol"}\n')
            with self.assertRaisesRegex(ValueError, "nonempty"):
                read_markers(path)


if __name__ == "__main__":
    unittest.main()
