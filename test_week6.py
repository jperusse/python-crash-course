""" Validation of week6 exercises """
import unittest
from week6 import User, Event
from week6 import create_user_report

class TestWeek6(unittest.TestCase):
    """ Final project: 
    Process a list of event objects using their date,
    type, machine, and user attributes to generate
    a report that lists all users currently logged into the machines.
    """

    def test_create_user_report_no_users(self):
        """ Create a user login/logout report for a list of events """
        event_list = []
        self.assertEqual(create_user_report(event_list), "no events found")

    def test_create_user_report_one_users(self):
        """ Create a user login/logout report for a list of events """
        user1 = User("Jim","jperusse")
        login = Event("12/1/2021", "login", "192.1.1.1", user1)
        event_list = [login]

        self.assertEqual(create_user_report(event_list), 
                         "192.1.1.1, 12/1/2021, login, jperusse, Jim")
