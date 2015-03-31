import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait

from signIn.TestConfig import TestConfig

class User2(unittest.TestCase, TestConfig):

	def setUp(self):
		TestConfig.setUp(self)		

	def testSignIn(self):
		driver = self.driver
		driver.get(self.test_url)
		element = driver.find_element_by_id("identity")
		element.send_keys("user-2@dlayer.com")
		element = driver.find_element_by_id("credentials")
		element.send_keys("password-2")
		element = driver.find_element_by_id("submit")
		element.send_keys(Keys.RETURN)
		self.assertIn("Dlayer.com - Web site development simplified", driver.title)
		TestConfig.signOut(self);

	def testIncorrectHostName(self):
		driver = self.driver
		driver.get(self.test_url)
		element = driver.find_element_by_id("identity")
		element.send_keys("user-2@dlayer.comm")
		element = driver.find_element_by_id("credentials")
		element.send_keys("password-2")
		element = driver.find_element_by_id("submit")
		element.click()
		self.assertTrue(driver.find_element_by_css_selector("div.has-error input#identity"))
		TestConfig.signOut(self);

	def testFailedSignNoPassword(self):
		driver = self.driver
		driver.get(self.test_url)
		element = driver.find_element_by_id("identity")
		element.send_keys("user-2@dlayer.com")
		element = driver.find_element_by_id("submit")
		element.click()
		self.assertTrue(driver.find_element_by_css_selector("div.has-error input#credentials"))
		TestConfig.signOut(self);

	def testFailedLogin(self):
		driver = self.driver
		driver.get(self.test_url)
		element = driver.find_element_by_id("identity")
		element.send_keys("user-4@dlayer.com")
		element = driver.find_element_by_id("credentials")
		element.send_keys("password-1")
		element = driver.find_element_by_id("submit")
		element.click()
		self.assertTrue(driver.find_element_by_css_selector("div.has-error input#identity"))
		TestConfig.signOut(self);

	def tearDown(self):
		TestConfig.tearDown(self)