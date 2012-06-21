import time

from selenium                       import webdriver
from django.test                    import LiveServerTestCase
from selenium.webdriver.common.keys import *
from django.contrib.contenttypes    import models as contenttypes_models

class CreationResponsableTest(LiveServerTestCase):
	fixtures = ['user_group.json']

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
		contenttypes_models.ContentType.objects.clear_cache()

	def test_login_via_admin_site(self):
		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys("admin")

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys("admin")
		password_field.send_keys(Keys.RETURN)

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)
		self.browser.get(self.live_server_url + '/admin/')
		self.browser.find_element_by_link_text('Log out').click()
		time.sleep(2)


	def test_add_new_responsable(self):
		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys("admin")

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys("admin")
		password_field.send_keys(Keys.RETURN)

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		self.browser.find_elements_by_link_text('Users')[0].click()
		self.browser.find_element_by_link_text('Add user').click()
		time.sleep(2)
		
		user_name  = self.browser.find_element_by_id('id_username')
		password_1 = self.browser.find_element_by_id('id_password1')
		password_2 = self.browser.find_element_by_id('id_password2')
		save_button = self.browser.find_element_by_name('_save')
		time.sleep(2)

		user_name.send_keys("Responsable_test")
		password_1.send_keys("Responsable_test")
		password_2.send_keys("Responsable_test")
		save_button.click()

		staff_status = self.browser.find_element_by_id('id_is_staff')
		staff_status.click()
		self.browser.find_element_by_name('_save').click()
		time.sleep(2)

		new_responsable_links = self.browser.find_elements_by_link_text("Responsable_test")
		self.assertEquals(len(new_responsable_links), 1)

		self.browser.get(self.live_server_url + '/admin/')
		self.browser.find_element_by_link_text('Log out').click()
		self.browser.get(self.live_server_url + '/admin/')

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys("Responsable_test")

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys("Responsable_test")
		password_field.send_keys(Keys.RETURN)

		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		self.browser.get(self.live_server_url + '/admin/')
		self.browser.find_element_by_link_text('Log out').click()
		time.sleep(2)