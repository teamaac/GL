from django.db import models

class TypeComposant(models.Model):
	label       = models.CharField(max_length = 255, unique = True)
	description = models.TextField()
	def __unicode__(self):
		return self.label

class VersionLogiciel(models.Model):
	label       = models.CharField(max_length=255, unique = True)
	description = models.TextField()
	def __unicode__(self):
		return self.label

class Nature(models.Model):
	label       = models.CharField(max_length=255, unique = True)
	description = models.TextField()
	def __unicode__(self):
		return self.label

class Licence(models.Model):
	label    = models.CharField(max_length=255, unique = True)
	gratuit  = models.BooleanField(default = False)
	libre    = models.BooleanField(default = False)
	contenu  = models.TextField()
	def __unicode__(self):
		return self.label

class Composant(models.Model):
	titre          = models.CharField(max_length = 255, unique = True)
	version        = models.ManyToManyField(VersionLogiciel, through = 'ComposantVersion')
	type_composant = models.ForeignKey(TypeComposant)
	def __unicode__(self):
		return self.titre

class ComposantVersion(models.Model):
	composant      = models.ForeignKey(Composant)
	version        = models.ForeignKey(VersionLogiciel)
	nature         = models.ForeignKey(Nature)
	license        = models.ForeignKey(Licence, default=1)
	cout           = models.FloatField(default = 0)
	def __unicode__(self):
		return "%s : %s" % (self.composant, self.version)

class Client(models.Model):
	designation  = models.CharField(max_length = 255)
	num_compte   = models.IntegerField()
	desscription = models.TextField()
	address      = models.TextField()
	def __unicode__(self):
		return self.designation

class Etat(models.Model):
	label       = models.CharField(max_length=255)
	description = models.TextField()
	def __unicode__(self):
		return self.label

class Produit(models.Model):
	titre       = models.CharField(max_length = 255, unique = True)
	version     = models.ManyToManyField(VersionLogiciel, through = 'ProduitVersion')
	description = models.TextField()
	def __unicode__(self):
		return self.titre

class ProduitVersion(models.Model):
	produit    = models.ForeignKey(Produit)
	version    = models.ForeignKey(VersionLogiciel)
	client     = models.ForeignKey(Client)
	etat       = models.ForeignKey(Etat)
	composants = models.ManyToManyField(ComposantVersion)
	def __unicode__(self):
		return "%s : %s" % (self.produit, self.version)