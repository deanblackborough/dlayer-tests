import unittest

from selenium import webdriver

from public.TestConfig import TestConfig

class DevelopmentLog(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)

	def testPageLoads(self):
		driver = self.driver
		driver.get(self.test_url + "/dlayer/index/development-log")
		self.assertIn("Development log", driver.title)

	def tearDown(self):
		TestConfig.tearDown(self)