""" week4 test class and methods """
import unittest
from week4 import format_address

class TestModule4GradedAssignment(unittest.TestCase):
    """ Week4 test class """
    def test_format_address(self):
        
        self.assertEqual(format_address("123 Main Street"),
                         '"house number 123 on street named Main Street"')

        self.assertEqual(format_address("1001 1st Ave"), 
                         '"house number 1001 on street named 1st Ave"')

        self.assertEqual(format_address("55 North Center Drive"),
                         '"house number 55 on street named North Center Drive"')
