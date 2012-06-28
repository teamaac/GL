from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ModificationEtat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
    
    def test_modification_etat(self):
        driver = self.driver
        driver.get(self.base_url + "admin/")
        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys("admin")
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys("admin")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Etats')])[2]").click()
        driver.find_element_by_link_text("Add etat").click()
        driver.find_element_by_id("id_label").clear()
        driver.find_element_by_id("id_label").send_keys("test")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("test")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_link_text("test").click()
        driver.find_element_by_id("id_label").clear()
        driver.find_element_by_id("id_label").send_keys("test 1")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_link_text("test 1").click()
        try: self.assertEqual("test 1", driver.find_element_by_id("id_label").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("test 2")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("test 1").click()
        try: self.assertEqual("test 2", driver.find_element_by_id("id_description").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("_save").click()
        driver.find_element_by_xpath("(//input[@name='_selected_action'])[7]").click()
        Select(driver.find_element_by_name("action")).select_by_visible_text("Delete selected etats")
        driver.find_element_by_name("index").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Log out").click()
        driver.get(self.base_url + "/admin/gestion/etat/")
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        try: self.assertEqual("test 2", driver.find_element_by_id("id_description").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
