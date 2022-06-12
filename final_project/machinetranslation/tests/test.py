import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_simple_word_notEqual(self):
        self.assertNotEqual(english_to_french("dog"), "a")

    def test_null(self):
        self.assertIsNone(english_to_french(None),None)

class TestFrenchToEnglish(unittest.TestCase):
    def test_simple_word(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_simple_word_notEqual(self):
        self.assertNotEqual(french_to_english("chien"), "a")

    def test_null(self):
        self.assertIsNone(french_to_english(None), None)

unittest.main()