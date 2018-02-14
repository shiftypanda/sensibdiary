from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class NewVisitorTest(LiveServerTestCase):
    """NewVisitorTest to check for how new user interacts with site"""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_record_a_sleep_and_retrieve_it_later(self):

        # Kirsty has heard about a cool new online sleep diary for children
        # with SEN. She goes to check out it's homepage

        self.browser.get(self.live_server_url)

        # She notices the page title and header mention SenSibDiary
        self.assertIn('SenSibDiary', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('SenSibDiary', header_text)
        # She is told straight away more about the sleep diary


        # She decides that she does want to enter some details and
        # She is invited to enter her login details or register


        # She registers for her username "Kirsty"
        # and enters a password "Password1".


        # After confirmed login she is then redirected to the sleep diary
        # This shows a list of all recent sleeps

        # There is also an option to view more detail about a sleep

        
        # She creates a named sleepers details

        # She enters a sleep diary for today's date

        # The page refreshes and it prompts to enter time started getting ready
        # for bed, time in bed and time went to sleep

        self.assertIs(False, "Finish test")
