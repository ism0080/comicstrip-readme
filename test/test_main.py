"""
Tests for main.py
"""

import unittest
import os
from main import get_dilbert, get_xkcd


class TestMain(unittest.TestCase):

    def test_dilbert(self):
        """Tests for downloading dilbert comic"""
        def test(env: str, result: str):
            os.environ["INPUT_SHOW_DILBERT"] = env
            self.assertEqual(get_dilbert(), result)
        test('false', "")
                
    def test_xkcd(self):
        """Tests for downloading xkcd comic"""
        def test(env: str, result: str):
            os.environ["INPUT_SHOW_XKCD"] = env
            self.assertEqual(get_xkcd(), result)
        test('false', "")

    def test_comicstrip(self):
        """Tests for the string added to the readme"""
        def test(dilbert: str, xkcd: str, result: str):
            os.environ["INPUT_SHOW_DILBERT"] = dilbert
            os.environ["INPUT_SHOW_XKCD"] = xkcd
            self.assertEqual(get_xkcd(), result)
        test('false', 'false', "")


if __name__ == '__main__':
    unittest.main()
