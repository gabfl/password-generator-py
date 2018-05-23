import unittest

from .. import pwgenerator


class Test(unittest.TestCase):

    def test_load_dictionary(self):
        dictionary = pwgenerator.load_dictionary()

        self.assertIsInstance(dictionary, tuple)

    def test_get_random_word(self):
        dictionary = pwgenerator.load_dictionary()

        self.assertIsInstance(pwgenerator.get_random_word(dictionary), str)

    def test_get_random_separator(self):
        self.assertIsInstance(pwgenerator.get_random_separator(), str)

    def test_get_random_int(self):
        self.assertTrue(pwgenerator.get_random_int(50) in range(51))

    def test_set_int_position(self):
        self.assertTrue(pwgenerator.set_int_position(4) in range(4))

    def test_pw(self):
        self.assertIsInstance(pwgenerator.pw(), str)

    def test_generate(self):
        self.assertIsInstance(pwgenerator.generate(), str)
