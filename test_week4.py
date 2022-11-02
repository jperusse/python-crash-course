""" week4 test class and methods """
import unittest

from week4 import format_address
from week4 import highlight_word
from week4 import combine_lists
from week4 import squares
from week4 import car_listing
from week4 import combine_guests


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

    def test_squares(self):
        """
        Create a list of squares for a given range.
        """
        self.assertEqual(squares(2,3), [4,9])
        self.assertEqual(squares(1,5), [1, 4, 9, 16, 25])
        self.assertEqual(squares(0,10), [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_car_listing(self):
        """
        Using a dictionary
        """
        self.assertEqual(
            car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}),
            "Kia Soul costs 19000 dollars\nLamborghini Diablo costs 55000 dollars\nFord Fiesta costs 13000 dollars\nToyota Prius costs 24000 dollars\n"
            )

    def test_combine_guests(self):
        """ Verify combine_guests """
        rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
        taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
        corrected_dict = { "David":1, "Nancy":1, "Robert":4, "Adam":2, "Samantha":3, "Chris":5, "Brenda":3, "Jose":3, "Charlotte":2, "Terry":1}
        guest_dict = combine_guests(rorys_guests, taylors_guests)
        self.assertDictEqual(guest_dict, corrected_dict)
