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
        self.assertIn('Jobs', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Jobs', header_text)
        
        # He can see the current running jobs of the pipeline immediatly
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any('umcg-ndeklein' in row.text for row in rows)
        )
        self.assertTrue(
            any('job_id' in row.text for row in rows)
        )
        # Clicking on the jobs shows which samples they are that are being run

        self.fail('Finish the test!')
if __name__ == '__main__': 
    unittest.main(warnings='ignore') 

