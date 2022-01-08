# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.common.exceptions import WebDriverException
from unittest import skip
from .base import FunctionalTest

# import time
# import unittest
# import os
# MAX_WAIT = 10
# class FunctionalTest(StaticLiveServerTestCase):
    
#     def setUp(self):
#         self.browser = webdriver.Firefox()
#         staging_server = os.environ.get('STAGING_SERVER')
#         if staging_server:
#             self.live_server_url = 'http://' + staging_server

#     def tearDown(self):
#         self.browser.quit()

#     def wait_for_row_in_list_table(self, row_text):
#         start_time = time.time()
#         while True:
#             try:
#                 table = self.browser.find_element_by_id('id_list_table')
#                 rows = table.find_elements_by_tag_name('tr')
#                 self.assertIn(row_text,[row.text for row in rows])
#                 return
#             except (AssertionError, WebDriverException) as e:
#                 if time.time() - start_time > MAX_WAIT:
#                     raise e
#                 time.sleep(0.5)

# class NewVisitorTest(FunctionalTest):

#     def test_can_start_a_list_and_retrieve_it_later(self):
#         # Edith has heard about a cool new online to-do app. She goes
#         # to check out its homepage
#         self.browser.get(self.live_server_url)
#         # self.browser.get('http://localhost:8000')

#         # She notices the page title and header mention to-do lists
#         self.assertIn('To-Do', self.browser.title)
#         header_text = self.browser.find_element_by_tag_name('h1').text
#         self.assertIn('To-Do', header_text)

#         # She is invited to enter a to-do item straight away
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

#         # She types "Buy peacock feathers" into a text box (Edith's hobby
#         # is tying fly-fishing lures)
#         inputbox.send_keys('Buy peacock feathers')
        
#         # When she hits enter, the page updates, and now the page lists
#         # "1: Buy peacock feathers" as an item in a to-do list
#         inputbox.send_keys(Keys.ENTER)
#         # time.sleep(1)
#         self.wait_for_row_in_list_table('1: Buy peacock feathers')

#         # There is still a text box inviting her to add another item. She
#         # enters "Use peacock feathers to make a fly" (Edith is very
#         # methodical)
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Use peacock feathers to make a fly')
#         inputbox.send_keys(Keys.ENTER)
#         # time.sleep(1)
#         self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
#         self.wait_for_row_in_list_table('1: Buy peacock feathers')
#         # table = self.browser.find_element_by_id('id_list_table')
#         # rows = table.find_elements_by_tag_name('tr')
#         # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
#         # self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
#         # There is still a text box inviting her to add another item. She
#         # enters "Use peacock feathers to make a fly" (Edith is very methodical)


#         # self.fail('Finish the test!')
        
#         # The page updates again, and now shows both items on her list

#         # Edith wonders whether the site will remember her list. Then she sees
#         # that the site has generated a unique URL for her -- there is some
#         # explanatory text to that effect.

#         # She visits that URL - her to-do list is still there.

#         # Satisfied, she goes back to sleep

#     def test_multiple_users_can_start_lists_at_different_urls(self):
#         #Edith starts a new to-do list
#         self.browser.get(self.live_server_url)
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Buy peacock feathers')
#         inputbox.send_keys(Keys.ENTER)
#         self.wait_for_row_in_list_table('1: Buy peacock feathers')

#         #She notices that her list has a unique URL
#         edith_list_url = self.browser.current_url
#         self.assertRegex(edith_list_url,'/lists/.+')

#         #Now a new user, Francis, comes along to the site.
#         #We use a new browser session to make sure that no information
#         #of edith's is coming through from cookies etc
#         self.browser.quit()
#         self.browser = webdriver.Firefox()

#         #Francis visits the home page. There is no sign of Edith's list
#         self.browser.get(self.live_server_url)
#         page_text= self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_text)
#         self.assertNotIn('make a fly', page_text)

#         #Francis starts a new list by entering a new item
#         #He is less interesting than Edith..
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         inputbox.send_keys('Buy milk')
#         inputbox.send_keys(Keys.ENTER)
#         self.wait_for_row_in_list_table('1: Buy milk')

#         #Francis gets his own unique URL
#         francis_list_url = self.browser.current_url
#         self.assertRegex(francis_list_url,'/lists/.+')
#         self.assertNotEqual(francis_list_url,edith_list_url)

#         #Again there is no trace of Edith's list
#         page_text = self.browser.find_element_by_tag_name('body').text
#         self.assertNotIn('Buy peacock feathers', page_text)
#         self.assertIn('Buy milk', page_text)

#         #Satisfied, they both go back to sleep
# class LayoutAndStylingTest(FunctionalTest):
#     def test_layout_and_styling(self):
#         #Edit goes to the home page
#         self.browser.get(self.live_server_url)
#         self.browser.set_window_size(1024, 768)

#         #She notices the inpux bos is nicely centered
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)

#         inputbox.send_keys('testing')
#         inputbox.send_keys(Keys.ENTER)
#         self.wait_for_row_in_list_table('1: testing')
#         inputbox = self.browser.find_element_by_id('id_new_item')
#         self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)
class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request, and does not load the
        # list page
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # She starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy wellies')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
        self.browser.find_element_by_css_selector('.has-error').text,
        "You've already got this in your list"
        ))

# if __name__ == '__main__':  
#     unittest.main(warnings='ignore')  