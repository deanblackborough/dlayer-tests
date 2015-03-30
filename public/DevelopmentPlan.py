import unittest

from selenium import webdriver

from public.TestConfig import TestConfig

class DevelopmentPlan(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)

	def testPageLoads(self):
		driver = self.driver
		driver.get(self.test_url + "/dlayer/index/development-plan")
		self.assertIn("Development plan", driver.title)

	def tearDown(self):
		TestConfig.tearDown(self)