import re
import inspect
from collections          import namedtuple
from gestion.tests.models import *

class SharedTest(object):
	def __init__(self, param=None):
		self.param = param
		if param != None:
			patch_model(param, patch_map[param])

	@staticmethod
	def publish_test(test_template):
		def test(self):
			if self.setup    : self.setup()
			test_template(self)
			if self.teardown : self.teardown()
		test.__name__= 'test_'+test_template.__name__
		return test

	def get_element(self, id, excepted_failure=False):
		try : 
			result = self.param.objects.get(pk = id)
			if excepted_failure: self.fail("Excepted DoesNotExist exception here")
			return result
		except self.param.DoesNotExist: 
			if not excepted_failure : self.fail("Not Excepted DoesNotExist exception here")

	def setup(self):
		self.test_element = self.param().generate()
		self.test_element.save()
		self.initial_element_count = len(self.param.objects.all())

	def teardown(self):pass

	def _tpl_selecting_an_existing_element_from_the_database(self):
		self.assertEquals(self.get_element(self.test_element.pk), self.test_element)

	def _tpl_selecting_non_existing_element_from_the_database(self):
		self.get_element(self.test_element.pk + 1, True)

	def _tpl_updating_an_existing_element_and_saving_it_to_the_database(self):
		self.test_element.generate().save()
		self.assertEquals(len(self.param.objects.all()), self.initial_element_count)
		self.assertEquals(self.get_element(self.test_element.pk), self.test_element)

	def _tpl_updating_an_existing_element_and_not_saving_it_to_the_database(self):
		self.test_element.generate()
		self.assertNotEquals(self.get_element(self.test_element.pk), self.test_element)

	def _tpl_delete_an_existing_element(self):
		self.param.delete(self.test_element)
		self.assertEquals(len(self.param.objects.all()), self.initial_element_count - 1)
		self.get_element(self.test_element.pk, True)

	def _tpl_delete_non_existing_element(self):
		self.param.delete(self.test_element)
		delete_error = False
		try:    self.param.delete(self.test_element)
		except: delete_error = True
		self.assertEquals(delete_error, True)