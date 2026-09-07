from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "toolkit"))
from steps import book_content


class BetaContentTests(unittest.TestCase):
    def test_beta_pack_has_expected_shape(self):
        self.assertEqual(
            book_content.check_beta(ROOT / "book"),
            {"prompts": 30, "workflows": 3, "sample_outputs": 13},
        )

    def test_every_prompt_chapter_is_represented(self):
        represented = {
            path.parents[1].name
            for path in (ROOT / "book" / "chapters").glob("0[1-9]-*/prompts/*.md")
        }
        self.assertEqual(len(represented), 9)


if __name__ == "__main__":
    unittest.main()
