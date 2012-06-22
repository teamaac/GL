from collections          import namedtuple
from gestion.tests.models import *

class SharedTest(object):
	def __init__(self, param=None):
		self.param = param
		if param != None:
			patch_model(param, patch_map[param])

	def create_and_save_new_element(self):
		result  = self.param().generate()
		result.save()
		return result

	def test_selecting_an_existing_element_from_the_database(self):
		element_test = self.create_and_save_new_element()
		specific_element_in_database  = self.param.objects.get(pk = element_test.pk)
		self.assertEquals(specific_element_in_database, element_test)

	def test_selecting_non_existing_element_from_the_database(self):
		element_test = self.create_and_save_new_element()
		all_element_in_database  = self.param.objects.all()
		self.assertEquals(len(all_element_in_database), 1)
		try : self.param.objects.get(pk = element_test.pk+1)
		except self.param.DoesNotExist: return
		self.fail("Excepted DoesNotExist exception here")

	def test_creating_a_new_element_and_saving_it_to_the_database(self):
		element_test = self.create_and_save_new_element()
		all_element_in_database  = self.param.objects.all()
		self.assertEquals(len(all_element_in_database), 1)
		self.assertEquals(all_element_in_database[0], element_test)

	def test_updating_an_existing_element_and_saving_it_to_the_database(self):
		element_test = self.create_and_save_new_element()
		element_test.generate()
		element_test.save()

		all_element_in_database  = self.param.objects.all()
		self.assertEquals(len(all_element_in_database), 1)
		self.assertEquals(all_element_in_database[0], element_test)

	def test_updating_an_existing_element_and_not_saving_it_to_the_database(self):
		element_test = self.create_and_save_new_element()
		element_test.generate()

		all_element_in_database  = self.param.objects.all()
		self.assertEquals(len(all_element_in_database), 1)
		self.assertNotEquals(all_element_in_database[0], element_test)

	def test_delete_an_existing_element(self):
		element_test = self.create_and_save_new_element()
		all_element_in_database  = self.param.objects.all()

		self.assertEquals(len(all_element_in_database), 1)
		self.assertEquals(all_element_in_database[0], element_test)
		self.param.delete(element_test)

		all_element_in_database  = self.param.objects.all()
		self.assertEquals(len(all_element_in_database), 0)

	def test_delete_non_existing_element(self):
		element_test = self.param().generate()
		all_element_in_database  = self.param.objects.all()

		self.assertEquals(len(all_element_in_database), 0)
		delete_error = False
		try:    self.param.delete(element_test)
		except: delete_error = True
		self.assertEquals(delete_error, True)