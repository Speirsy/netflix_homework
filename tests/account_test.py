import unittest
from src.account import *
from src.profile import *
from src.movie import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")
     
        self.account_1 = Account("Jane", "Smith", "janes@email.com")


    # Test an Account can add a Profile

    def test_account_can_add_profile(self):
        self.account_1.add_profile(self.profile_1)  
        self.assertEqual(1, self.account_1.number_of_profiles())

    # Test an Account can remove a given Profile

    def test_account_can_remove_profile(self):
        self.account_1.add_profile(self.profile_1)
        self.account_1.remove_profile(self.profile_1)
        self.assertEqual(0, self.account_1.number_of_profiles())

    # Test an Account can return a list of Profiles

    def test_account_can_return_list_of_profiles(self):
        self.account_1.add_profile(self.profile_1)
        self.account_1.add_profile(self.profile_2)
        # self.assertEqual((self.account_1, self.account_2) self.list_of_profiles)

# probably a for loop required to loop through self.profiles
# dunno


        



    # Test an Account can return a list of Profiles

   
