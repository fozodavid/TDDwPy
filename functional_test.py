from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Mr.Cain heard about a cool new online todo app.
		#He goes to check out the homepage.
		self.browser.get('http://localhost:8000')

		#He notices that header and title mentions todo list
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		#He is invited to enter todo items straight away

		#He types buy custom Cain rifle into a text box

		#When he hits enter, the page updates, and now the page lists
		#"1: buy custom Cain rifle" as an item in a to-do list

		#There is still a text box inviting him to add another item. He
		#enters "Sharpen blade"

		#The page updates again, and now shows both items on the list

		#Mr.Cain wonders whether the site will remember his list. The he sees
		#that the site has generated a unique URL for him -- there is some
		#explanatory text to that effect.

		#He visits that URL - his to-do list is still there.

		#Satisfied, he goes back to sleep.

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')