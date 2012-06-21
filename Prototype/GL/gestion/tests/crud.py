from django.test              import TestCase
from gestion.tests.models     import *
from gestion.tests.sharedtest import SharedTest

def test_case_factory(ModelClass):
	class X(TestCase, SharedTest):
		def __init__(self, methodName='runTest'):
			TestCase  .__init__(self, methodName)
			SharedTest.__init__(self, ModelClass)
	X.__name__ = "%sTest" % (ModelClass.__name__,)
	return X

EtatTest                           = test_case_factory(Etat)
NatureTest                         = test_case_factory(Nature)
ClientTest                         = test_case_factory(Client)
LicenceTest                        = test_case_factory(Licence)
ProduitTest                        = test_case_factory(Produit)
ComposantTest                      = test_case_factory(Composant)
TypeComposantTest                  = test_case_factory(TypeComposant)
ProduitVersionTest                 = test_case_factory(ProduitVersion)
VersionLogicielTest                = test_case_factory(VersionLogiciel)
ComposantVersionTest               = test_case_factory(ComposantVersion)
ProduitVersionComposantVersionTest = test_case_factory(ProduitVersionComposantVersion)