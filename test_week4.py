""" week4 test class and methods """
import unittest
from week4 import format_address, highlight_word, combine_lists


class TestWeek4(unittest.TestCase):
    """ Week4 test class """

    def test_format_address(self):
        """ Verify format_address """
        self.assertEqual(format_address("123 Main Street"),
                         '"house number 123 on street named Main Street"')

        self.assertEqual(format_address("1001 1st Ave"),
                         '"house number 1001 on street named 1st Ave"')

        self.assertEqual(format_address("55 North Center Drive"),
                         '"house number 55 on street named North Center Drive"')

    def test_highlight_word(self):
        """ Use all CAPS to highlight a word in a sentence """
        self.assertEqual(highlight_word("Have a nice day", "nice"),
                         "Have a NICE day")

        self.assertEqual(highlight_word("Shhh, don't be so loud!", "loud"),
                         "Shhh, don't be so LOUD!")

        self.assertEqual(highlight_word("Automating with Python is fun", "fun"),
                         "Automating with Python is FUN")

        self.assertEqual(highlight_word("Automating with Python is fun", "Automating"),
                         "AUTOMATING with Python is fun")

    def test_combine_lists(self):
        """ combine two lists reversing the first """
        jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
        drews_list = ["Mike", "Carol", "Greg", "Marcia"]

        self.assertEqual(combine_lists(jamies_list, drews_list),
                         ['Mike', 'Carol', 'Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Alice']
        )
