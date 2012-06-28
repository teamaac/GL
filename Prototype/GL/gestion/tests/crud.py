import sys
from django.test              import TestCase
from gestion.tools            import template_tests
from gestion.tools            import nonabstract_models
from gestion.tests.sharedtest import SharedTest

def init_shared_tests(models_module):
    map(SharedTest.publish_test, template_tests(models_module))
    for model in nonabstract_models(models_module):
        class Template(TestCase, SharedTest):
            def __init__(self, method_name='runTest'):
                TestCase  .__init__(self, method_name)
                SharedTest.__init__(self, model[1]   )
        Template.__name__ = model[1].__name__+"Test"
        setattr(sys.modules[globals()['__name__']], Template.__name__, Template)