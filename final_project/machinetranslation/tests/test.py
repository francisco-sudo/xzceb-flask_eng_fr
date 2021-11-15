import unittest
import translator

class TestSquareE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french(''), 'Bonjour') 
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour') 


class TestSquareF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english(''), 'Hello') 
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello' ) 

unittest.main()