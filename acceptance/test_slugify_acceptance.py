"""Owner-approved acceptance tests. Protected: candidates must not edit this file."""
import importlib
import unittest


class SlugifyAcceptance(unittest.TestCase):
    def setUp(self):
        self.slugify = importlib.import_module("canary.slugify").slugify

    def test_examples(self):
        cases = {
            " Hello, World! ": "hello-world",
            "A___B": "a-b",
            "  ---  ": "",
            "  123  ": "123",
            "Already-slug": "already-slug",
            "Ünïcode Ünits": "n-code-nits",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(self.slugify(text), expected)

    def test_returns_str(self):
        self.assertIsInstance(self.slugify("x"), str)


if __name__ == "__main__":
    unittest.main()
