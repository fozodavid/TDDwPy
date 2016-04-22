import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

class NewVisitorTest(StaticLiveServerTestCase):


	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	# @classmethod
	# def tearDownClass(cls):
	# 	if cls.server_url == cls.live_server_url:
	# 		super().tearDownClass()

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# def test_layout_and_styling(self):
	# 	#Mr.Cain goes to the homepage
	# 	self.browser.get(self.server_url)
	# 	self.browser.set_window_size(1024, 768)

	# 	#She notices the input box is nicely centered
	# 	inputbox = self.browser.find_element_by_id('id_new_item')
	# 	inputbox.send_keys('testing\n')
	# 	self.assertAlmostEqual(
	# 		inputbox.location['x'] + inputbox.size['width'] / 2,
	# 		512,
	# 		delta = 5
	# 	)

	def check_for_row_in_list_tabel(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows  = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Mr.Cain heard about a cool new online todo app.
		#He goes to check out the homepage.
		self.browser.get(self.server_url)

		#He notices that header and title mentions todo list
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#He is invited to enter todo items straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a To-Do item'

		)

		#He types buy custom Cain rifle into a text box
		inputbox.send_keys('buy custom Cain rifle')

		#When he hits enter, the page updates, and now the page lists
		#"1: buy custom Cain rifle" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_tabel('1: buy custom Cain rifle')

		#There is still a text box inviting him to add another item. He
		#enters "Sharpen blade"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('sharpen blade')
		inputbox.send_keys(Keys.ENTER)
		#The page updates again, and now shows both items on the list
		self.check_for_row_in_list_tabel('1: buy custom Cain rifle')
		self.check_for_row_in_list_tabel('2: sharpen blade')

		self.browser.implicitly_wait(3)

		#Mr.Cain wonders whether the site will remember his list. The he sees
		#that the site has generated a unique URL for him -- there is some
		#explanatory text to that effect.


		#He visits that URL - his to-do list is still there.

		#Satisfied, he goes back to sleep.

	@skip
	def test_cannot_add_empty_list_items(self):
		# Mr.Cain goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box

		# The home page refreshes, and there is an error message saying 
		# that list items cannot be blank

		# She tries again with some text for the item, which now works

		# Perversely, she now decides to submit a second blank list item

		# She receives a similar warming on the list page

		# And she can correct it by filling some text in
		self.fail('write me!')

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')