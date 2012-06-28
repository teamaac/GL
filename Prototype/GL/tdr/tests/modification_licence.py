from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ModificationLicence(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
    
    def test_modification_licence(self):
        driver = self.driver
        driver.get(self.base_url + "admin/")
        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys("admin")
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys("admin")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Licences')])[2]").click()
        driver.find_element_by_link_text("Add licence").click()
        driver.find_element_by_id("id_label").clear()
        driver.find_element_by_id("id_label").send_keys("Test Licence")
        driver.find_element_by_id("id_gratuit").click()
        driver.find_element_by_id("id_libre").click()
        driver.find_element_by_id("id_contenu").clear()
        driver.find_element_by_id("id_contenu").send_keys("test")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_link_text("Test Licence").click()
        driver.find_element_by_id("id_label").clear()
        driver.find_element_by_id("id_label").send_keys("Test Licence 2")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_link_text("Test Licence 2").click()
        try: self.assertEqual("Test Licence 2", driver.find_element_by_id("id_label").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("id_gratuit").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Test Licence 2").click()
        try: self.assertEqual("off", driver.find_element_by_id("id_gratuit").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("id_libre").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Test Licence 2").click()
        try: self.assertEqual("off", driver.find_element_by_id("id_libre").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("id_contenu").clear()
        driver.find_element_by_id("id_contenu").send_keys("test 2")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Test Licence 2").click()
        try: self.assertEqual("test 2", driver.find_element_by_id("id_contenu").get_attribute("value"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("_save").click()
        driver.find_element_by_xpath("(//input[@name='_selected_action'])[3]").click()
        Select(driver.find_element_by_name("action")).select_by_visible_text("Delete selected licences")
        driver.find_element_by_name("index").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
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
