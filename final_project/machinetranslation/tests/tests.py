# test_simple_unittest.py
import unittest
import sys
sys.path.append(".")
import translator


class TestMethods(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertEqual(translator.french_to_english(None), '')

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertEqual(translator.english_to_french(None), '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
