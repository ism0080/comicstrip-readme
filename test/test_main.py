"""
Tests for main.py
"""

import unittest
import os
from main import get_xkcd


class TestMain(unittest.TestCase):

    def test_xkcd(self):
        """Tests for downloading xkcd comic"""
        def test(env: str, result: str):
            os.environ["INPUT_SHOW_XKCD"] = env
            self.assertEqual(get_xkcd(), result)
        test('false', "")

    def test_comicstrip(self):
        """Tests for the string added to the readme"""
        def test(xkcd: str, result: str):
            os.environ["INPUT_SHOW_XKCD"] = xkcd
            self.assertEqual(get_xkcd(), result)
        test('false', "")


if __name__ == '__main__':
    unittest.main()
