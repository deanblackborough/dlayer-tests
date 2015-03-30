import unittest

from selenium import webdriver

from public.TestConfig import TestConfig

class Bugs(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)

	def testPageLoads(self):
		driver = self.driver
		driver.get(self.test_url + "/dlayer/index/bugs")
		self.assertIn("Known bugs", driver.title)

	def tearDown(self):
		TestConfig.tearDown(self)