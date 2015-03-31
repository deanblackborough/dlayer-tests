import unittest

from selenium import webdriver

from signIn.TestConfig import TestConfig

class Home(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)

	# def testPageLoads(self):
	# 	driver = self.driver
	# 	driver.get(self.test_url)
	# 	self.assertIn("Dlayer.com - Sign in", driver.title)

	def tearDown(self):
		TestConfig.tearDown(self)