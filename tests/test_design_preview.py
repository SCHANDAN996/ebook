from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "toolkit"))
import book_design_preview


class DesignPreviewTests(unittest.TestCase):
    def test_preview_has_five_pages_bookmarks_and_copy_companion(self):
        try:
            from pypdf import PdfReader
        except ImportError:
            self.skipTest("pypdf optional PDF dependency is not installed")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pdf, companion = book_design_preview.run(root / "preview.pdf", root / "preview.html")
            reader = PdfReader(str(pdf))
            self.assertEqual(len(reader.pages), 5)
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            self.assertIn("COPY-PASTE PROMPT", text)
            self.assertIn("ILLUSTRATIVE DRAFT", text)
            self.assertIn("HUMAN GATE", text)
            self.assertGreaterEqual(len(reader.outline), 5)
            annotations = [a for page in reader.pages for a in (page.get("/Annots") or [])]
            self.assertTrue(annotations)
            html_text = companion.read_text(encoding="utf-8")
            self.assertIn("navigator.clipboard.writeText", html_text)
            self.assertIn("aria-live=\"polite\"", html_text)


if __name__ == "__main__":
    unittest.main()

