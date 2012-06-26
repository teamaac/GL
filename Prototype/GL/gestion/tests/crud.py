import re, sys, gestion.models
from inspect                  import ismethod, isclass, getmembers
from django.test              import TestCase
from gestion.tests.sharedtest import SharedTest

map(SharedTest.publish_test, filter(re.compile('^_tpl_.*').search, [x[0] for x in getmembers(SharedTest, ismethod)]))

for i in getmembers(gestion.models, lambda c: isclass(c) and not c._meta.abstract):
	class X(TestCase, SharedTest):
		def __init__(self, methodName='runTest'):
			TestCase  .__init__(self, methodName)
			SharedTest.__init__(self, i[1]      )
	X.__name__ = i[1].__name__+"Test"
	setattr(sys.modules[globals()['__name__']], X.__name__, X)
	X = None