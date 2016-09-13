from number_namer import *
import unittest

class TestNumberNamer(unittest.TestCase):

    def test_digit(self):
        self.assertEqual(name_of_digit(1), "one")
        self.assertEqual(name_of_digit(5), "five")

    def test_tens(self):
        self.assertEqual(name_of_tens(2), "twenty")
        self.assertEqual(name_of_tens(4), "forty")

    def test_teens(self):
        self.assertEqual(name_of_teens(13), "thirteen")
        self.assertEqual(name_of_teens(17), "seventeen")

    def test_integer(self):
        self.assertEqual(name_of_integer(999999999), "nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine")
        self.assertEqual(name_of_integer(280398400), "two hundred eighty million three hundred ninety eight thousand four hundred")

    def test_fraction(self):
        self.assertEqual(name_of_fraction((1, 10)), "one tenth")
        self.assertEqual(name_of_fraction((2, 100)), "two hundredths")

    def test_devimal(self):
        self.assertEqual(name_of_decimal(98, (7, 10)), "ninety eight and seven tenths")
        self.assertEqual(name_of_decimal(48, (2, 100)), "forty eight and two hundredths")

    def test_dollars(self):
        self.assertEqual(name_in_dollars(0, 7), "seven cents")
        self.assertEqual(name_in_dollars(12, 7), "twelve dollars and seven cents")

    def test_nameofnumber(self):
        self.assertEqual(name_of_number("2015"), "two thousand fifteen")
        self.assertEqual(name_of_number("$23.30"), "twenty three dollars and thirty cents")
                         
unittest.main()
