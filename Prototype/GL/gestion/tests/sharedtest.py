from autofixture         import *
from gestion.tests.tools import *

class SharedTest(object):
	def __init__(self, param):
		self.param        = param
		self.param.__eq__ = compare

	@staticmethod
	def publish_test(test_template):
		def test(self):
			self.setup()
			getattr(self, test_template)()
			self.teardown()
		test.__name__= 'test_'+test_template
		setattr(SharedTest, test.__name__, test)

	def get_element(self, id, excepted_failure=False):
		try : 
			result = self.param.objects.get(pk = id)
			if excepted_failure: self.fail("Excepted DoesNotExist exception here")
			return result
		except self.param.DoesNotExist: 
			if not excepted_failure : self.fail("Not Excepted DoesNotExist exception here")

	def setup(self):
		self.fixture      = AutoFixture(self.param)
		self.test_element = self.fixture.create_one()
		self.initial_element_count = len(self.param.objects.all())

	def teardown(self): pass

	def _tpl_selecting_an_existing_element_from_the_database(self):
		self.assertEquals(self.get_element(self.test_element.pk), self.test_element)

	def _tpl_selecting_non_existing_element_from_the_database(self):
		self.get_element(self.test_element.pk + 1, True)

	def _tpl_updating_an_existing_element_and_saving_it_to_the_database(self):
		self.fixture.generate(self.test_element).save()
		self.assertEquals(len(self.param.objects.all()), self.initial_element_count)
		self.assertEquals(self.get_element(self.test_element.pk), self.test_element)

	def _tpl_updating_an_existing_element_and_not_saving_it_to_the_database(self):
		self.fixture.generate(self.test_element)
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