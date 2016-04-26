
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Mr.Cain heard about a cool new online todo app.
		#He goes to check out the homepage.
		self.browser.get(self.server_url)

		#He notices that header and title mentions todo list
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#He is invited to enter todo items straight away
		inputbox = self.browser.find_element_by_id('id_text') # need to be revised problem with inheritance 
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a To-Do item'

		)

		#He types buy custom Cain rifle into a text box
		inputbox.send_keys('buy custom Cain rifle')

		#When he hits enter, the page updates, and now the page lists
		#"1: buy custom Cain rifle" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: buy custom Cain rifle')

		#There is still a text box inviting him to add another item. He
		#enters "Sharpen blade"
		inputbox = self.browser.find_element_by_id('id_text')
		inputbox.send_keys('sharpen blade')
		inputbox.send_keys(Keys.ENTER)
		#The page updates again, and now shows both items on the list
		self.check_for_row_in_list_table('1: buy custom Cain rifle')
		self.check_for_row_in_list_table('2: sharpen blade')

		self.browser.implicitly_wait(3)

		#Mr.Cain wonders whether the site will remember his list. The he sees
		#that the site has generated a unique URL for him -- there is some
		#explanatory text to that effect.


		#He visits that URL - his to-do list is still there.

		#Satisfied, he goes back to sleep