import unittest

from selenium import webdriver

from public.TestConfig import TestConfig

class HistoryOfDlayer(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)

	def test_page_loads(self):
		driver = self.driver
		driver.get(self.test_url + "/dlayer/index/dlayer-history")
		self.assertIn("The history of Dlayer", driver.title)

	def tearDown(self):
		TestConfig.tearDown(self)