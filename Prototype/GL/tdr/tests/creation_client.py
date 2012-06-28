import re
from django.test      import LiveServerTestCase
from tdr.tests.common import *

class CreationClient(LiveServerTestCase):
    def setUp(self):
        webdriver_setup(self)

    def tearDown(self):
        generic_tear_down(self)

    def test_creation_client(self):
        driver.get(self.base_url + "/admin/")
        set_input(self, "id_username", "admin")
        set_input(self, "id_password", "admin")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_css_selector("#module_2 > div.dashboard-module-content > ul > li > a").click()
        driver.find_element_by_link_text("Add client").click()
        set_input(self, "id_designation" , "client 1")
        set_input(self, "id_num_compte"  , "001"     )
        set_input(self, "id_desscription", "test"    )
        set_input(self, "id_address"     , "test"    )
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_xpath("(//a[contains(text(),'Gestion')])[2]").click()
        driver.find_element_by_xpath("//div[@id='module_1']/div/ul/li[11]/ul/li/a/span").click()
        set_input(self, "id_designation" , "client 2")
        set_input(self, "id_num_compte"  , "002"     )
        set_input(self, "id_desscription", "test"    )
        set_input(self, "id_address"     , "test"    )
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_id("action-toggle").click()
        Select(driver.find_element_by_name("action")).select_by_visible_text("Delete selected clients")
        driver.find_element_by_name("index").click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Log out").click()