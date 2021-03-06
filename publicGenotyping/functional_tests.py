import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
#        caps = DesiredCapabilities.FIREFOX
#        caps["marionette"] = True
#        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_see_the_jobs(self):
        # Gene wants to look at the progress of his compute pipelines on a web-app
        # and goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)  

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

               
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')


        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fail('Finish the test!')
        
    
# The page updates again, and now shows both items on her list
if __name__ == '__main__': 
    unittest.main(warnings='ignore') 

