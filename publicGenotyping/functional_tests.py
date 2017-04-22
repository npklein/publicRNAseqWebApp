from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=caps)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_see_the_jobs(self):
        # Gene wants to look at the progress of his compute pipelines on a web-app
        # and goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention PublicGenotyping
        self.assertIn('PublicGenotyping', self.browser.title)
        self.fail('Finish the test!')
        # He can see the current running jobs of the pipeline immediatly

        # Clicking on the jobs shows which samples they are that are being run


if __name__ == '__main__': 
    unittest.main(warnings='ignore') 

