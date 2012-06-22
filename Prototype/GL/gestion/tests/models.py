import string
import random
from django.db      import models
from gestion.models import *

def string_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for x in range(size))

def compare(self, other):
	if not(isinstance(other, self.__class__) and self._get_pk_val() == other._get_pk_val()) : return False
	old, new      = {}, {}
	dt_1, dt_2    = self.__dict__, other.__dict__
	excluded_keys = 'created', '_state', 'timestamp', 'user', 'uid', 'changed'
	for k,v in dt_1.items():
		try:
			if k in excluded_keys: continue
			if v != dt_2[k]:
				if type(v) is float:
					return abs(v-dt_2[k]) < 1e-4
				else:
					return False
		except KeyError: pass
	return True

def patch_model(modelclass, generator):
	if issubclass(modelclass, models.Model) :
		modelclass.generate = generator
		modelclass.__eq__   = compare
	else:
		raise TypeError("Can only patch non model class")

def abstract_info_generator(model_instance):
	model_instance.label       = string_generator()
	model_instance.description = string_generator()
	return model_instance

def licence_generator(model_instance):
	model_instance.label   = string_generator()
	model_instance.gratuit = bool(random.getrandbits(1))
	model_instance.libre   = bool(random.getrandbits(1))
	model_instance.contenu = string_generator()
	return model_instance

def client_generator(model_instance):
	model_instance.designation = string_generator()
	model_instance.num_compte  = random.randint(0,10000)
	model_instance.description = string_generator()
	model_instance.address     = string_generator()
	return model_instance

def composant_generator(model_instance):
	model_instance.titre          = string_generator()
	model_instance.type_composant = abstract_info_generator(TypeComposant())
	model_instance.type_composant.save()
	model_instance.type_composant_id = model_instance.type_composant.pk
	return model_instance

def composant_version_generator(model_instance):
	model_instance.composant = composant_generator(Composant())
	model_instance.composant.save()
	model_instance.composant_id = model_instance.composant.pk
	model_instance.version      = abstract_info_generator(VersionLogiciel())
	model_instance.version.save()
	model_instance.version_id = model_instance.version.pk
	model_instance.nature     = abstract_info_generator(Nature())
	model_instance.nature.save()
	model_instance.nature_id = model_instance.nature.pk
	model_instance.licence   = abstract_info_generator(Licence())
	model_instance.licence.save()
	model_instance.licence_id = model_instance.licence.pk
	model_instance.cout       = random.uniform(1.0, 5.0) * random.randint(10,10000)
	return model_instance

def produit_generator(model_instance):
	model_instance.titre       = string_generator()
	model_instance.description = string_generator()
	return model_instance

def produit_version_generator(model_instance):
	model_instance.produit    = produit_generator(Produit())
	model_instance.produit.save()
	model_instance.produit_id = model_instance.produit.pk
	model_instance.version    = abstract_info_generator(VersionLogiciel())
	model_instance.version.save()
	model_instance.version_id = model_instance.version.pk
	model_instance.client     = client_generator(Client())
	model_instance.client.save()
	model_instance.client_id  = model_instance.client.pk
	model_instance.etat       = abstract_info_generator(Etat())
	model_instance.etat.save()
	model_instance.etat_id    = model_instance.etat.pk
	return model_instance

def produit_version_composant_version_generator(model_instance):
	model_instance.produit_version   = produit_version_generator(ProduitVersion())
	model_instance.produit_version.save()
	model_instance.produit_version_id = model_instance.produit_version.pk
	model_instance.composant_version  = composant_version_generator(ComposantVersion())
	model_instance.composant_version.save()
	model_instance.composant_version_id = model_instance.composant_version.pk
	return model_instance

patch_map = {
	Etat                           : abstract_info_generator                    ,
	Nature                         : abstract_info_generator                    ,
	Client                         : client_generator                           ,
	Licence                        : licence_generator                          ,
	Produit                        : produit_generator                          ,
	Composant                      : composant_generator                        ,
	TypeComposant                  : abstract_info_generator                    ,
	ProduitVersion                 : produit_version_generator                  ,
	VersionLogiciel                : abstract_info_generator                    ,
	ComposantVersion               : composant_version_generator                ,
	ProduitVersionComposantVersion : produit_version_composant_version_generator,
}