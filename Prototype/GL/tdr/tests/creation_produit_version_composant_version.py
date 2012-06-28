from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CreationProduitVersionComposantVersion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
    
    def test_creation_produit_version_composant_version(self):
        driver = self.driver
        driver.get(self.base_url + "admin/")
        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys("admin")
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys("admin")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Produit version composant versions')])[2]").click()
        driver.find_element_by_link_text("Add produit version composant version").click()
        driver.find_element_by_css_selector("img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_css_selector("img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("id_titre").clear()
        driver.find_element_by_id("id_titre").send_keys("produit 1")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("test")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_css_selector("#add_id_version > img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("id_label").clear()
        driver.find_element_by_id("id_label").send_keys("0.1")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("aezraezr")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_css_selector("#add_id_client > img[alt=\"Add Another\"]").click()
        driver.find_element_by_css_selector("#add_id_client > img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("id_designation").clear()
        driver.find_element_by_id("id_designation").send_keys("client 1")
        driver.find_element_by_id("id_num_compte").clear()
        driver.find_element_by_id("id_num_compte").send_keys("001")
        driver.find_element_by_id("id_desscription").clear()
        driver.find_element_by_id("id_desscription").send_keys("zfsdfqsdf")
        driver.find_element_by_id("id_address").clear()
        driver.find_element_by_id("id_address").send_keys("qsdfqsdf")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        Select(driver.find_element_by_id("id_etat")).select_by_visible_text("Analyse")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_css_selector("#add_id_composant_version > img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        driver.find_element_by_css_selector("#add_id_composant_version > img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("add_id_composant").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_id("id_titre").clear()
        driver.find_element_by_id("id_titre").send_keys("cmp1")
        Select(driver.find_element_by_id("id_type_composant")).select_by_visible_text("Open Source")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        Select(driver.find_element_by_id("id_version")).select_by_visible_text("0.1")
        Select(driver.find_element_by_id("id_nature")).select_by_visible_text("dll")
        Select(driver.find_element_by_id("id_licence")).select_by_visible_text("GPL v3")
        driver.find_element_by_id("id_cout").clear()
        driver.find_element_by_id("id_cout").send_keys("100")
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow]]
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_name("_selected_action").click()
        Select(driver.find_element_by_name("action")).select_by_visible_text("Delete selected produit version composant versions")
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
