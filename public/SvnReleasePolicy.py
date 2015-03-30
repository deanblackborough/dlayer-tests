import unittest

from selenium import webdriver

from public.TestConfig import TestConfig

class SvnReleasePolicy(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)

	def testPageLoads(self):
		driver = self.driver
		driver.get(self.test_url + "/dlayer/index/svn-release-policy")
		self.assertIn("SVN & release policy", driver.title)

	def tearDown(self):
		TestConfig.tearDown(self)