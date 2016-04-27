# from unittest import skip
from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_duplicate_items(self):
		# Cain goes to the home page and start a new list
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('Buy wellies\n')
		self.check_for_row_in_list_table('1: Buy wellies')

		# He accidentally tries to enter a duplicate item
		self.get_item_input_box().send_keys('Buy wellies\n')

		# He sees helpful error message
		self.check_for_row_in_list_table('1: Buy wellies')
		error = self.browser.find_element_by_class_name('errorlist')
		self.assertEqual(error.text, "You've already got this in your list")



	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')

	def test_cannot_add_empty_list_items(self):
		# Mr.Cain goes to the home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_text').send_keys('\n')

		# The home page refreshes, and there is an error message saying 
		# that list items cannot be blank
		error = self.browser.find_element_by_class_name('errorlist')
		self.assertEqual(error.text, "You can't have an empty list item")

		# She tries again with some text for the item, which now works
		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		# Perversely, she now decides to submit a second blank list item
		self.get_item_input_box().send_keys('\n')

		# She receives a similar warming on the list page
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_class_name('errorlist')
		self.assertEqual(error.text, "You can't have an empty list item")

		# And she can correct it by filling some text in
		self.get_item_input_box().send_keys('Make Tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make Tea')
