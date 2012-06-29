import re
import inspect

from django.db.models.fields.related import ReverseManyRelatedObjectsDescriptor
from django.db.models.fields.related import ReverseSingleRelatedObjectDescriptor

def is_abstract_model_predicate(obj):
    return inspect.isclass(obj) and not obj._meta.abstract

def is_foreign_key_predicate(obj):
    return inspect.isdatadescriptor(obj) and isinstance(obj, ReverseSingleRelatedObjectDescriptor)

def is_many_to_many_predicate(obj):
    return inspect.isdatadescriptor(obj) and isinstance(obj, ReverseManyRelatedObjectsDescriptor)

def module_classes(module):
    return inspect.getmembers(module, inspect.isclass)

def nonabstract_models(models_module):
    return inspect.getmembers(models_module, is_abstract_model_predicate)

def foreignkey_fields(model):
    return map(lambda x: (x[0],x[1].field.rel.to), inspect.getmembers(model, is_foreign_key_predicate))

def many_to_many_fields(model):
    return map(lambda x: (x[0],x[1].field.rel.to), inspect.getmembers(model, is_many_to_many_predicate))

def template_tests(module):
    template_regex = re.compile('^_tpl_.*')
    return filter(template_regex.search, [x[0] for x in inspect.getmembers(module, inspect.ismethod)])