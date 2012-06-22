from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SuppressionVersionLogiciel(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://localhost:8000/"
		self.verificationErrors = []
	
	def test_suppression_version_logiciel(self):
		driver = self.driver
		driver.get(self.base_url + "admin/")
		username_field = self.driver.find_element_by_name('username')
		username_field.send_keys("admin")
		password_field = self.driver.find_element_by_name('password')
		password_field.send_keys("admin")
		driver.find_element_by_css_selector("input[type=\"submit\"]").click()
		driver.find_element_by_xpath("(//a[contains(text(),'Version logiciels')])[2]").click()
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		driver.find_element_by_link_text("Add version logiciel").click()
		driver.find_element_by_id("id_label").clear()
		driver.find_element_by_id("id_label").send_keys("0.1")
		driver.find_element_by_id("id_description").clear()
		driver.find_element_by_id("id_description").send_keys("test")
		driver.find_element_by_name("_save").click()
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		driver.find_element_by_link_text("Add version logiciel").click()
		driver.find_element_by_id("id_label").clear()
		driver.find_element_by_id("id_label").send_keys("0.2")
		driver.find_element_by_id("id_description").clear()
		driver.find_element_by_id("id_description").send_keys("test")
		driver.find_element_by_name("_save").click()
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		driver.find_element_by_name("_selected_action").click()
		driver.find_element_by_css_selector("tr.row2 > td.action-checkbox > input[name=\"_selected_action\"]").click()
		Select(driver.find_element_by_name("action")).select_by_visible_text("Delete selected version logiciels")
		driver.find_element_by_name("index").click()
		driver.find_element_by_css_selector("input[type=\"submit\"]").click()
		# ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
		driver.find_element_by_link_text("Log out").click()
	
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
