from selenium import webdriver

class TestConfig():
	test_url = 'http://dlayer.dev'

	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		self.driver.close()