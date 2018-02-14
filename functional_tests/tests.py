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

        # She notices the page title and header mention sleep diary

        # She is told straight away more about the sleep diary

        # She decides that she does want to enter some details and
        # She is invited to enter her login details or register

        # She registers for her username "Kirsty" and enters a password "Password1"

        # After confirmed login she is then redirected to enter a sleep diary
        
