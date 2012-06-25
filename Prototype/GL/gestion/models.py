from django.db import models

class AbstractInfo(models.Model):
	label       = models.CharField(max_length = 255, unique = True)
	description = models.TextField()
	class Meta           : abstract = True
	def __unicode__(self): return self.label

class Etat           (AbstractInfo):pass
class Nature         (AbstractInfo):pass
class TypeComposant  (AbstractInfo):pass
class VersionLogiciel(AbstractInfo):pass

class Licence(models.Model):
	label    = models.CharField(max_length = 255, unique = True)
	gratuit  = models.BooleanField(default = False)
	libre    = models.BooleanField(default = False)
	contenu  = models.TextField()
	def __unicode__(self): return self.label

class Composant(models.Model):
	titre          = models.CharField(max_length = 255, unique = True)
	versions       = models.ManyToManyField(VersionLogiciel, through = 'ComposantVersion')
	description    = models.TextField()
	type_composant = models.ForeignKey(TypeComposant)
	def __unicode__(self): return self.titre

class ComposantVersion(models.Model):
	composant      = models.ForeignKey(Composant)
	version        = models.ForeignKey(VersionLogiciel)
	nature         = models.ForeignKey(Nature)
	licence        = models.ForeignKey(Licence)
	cout           = models.FloatField(default = 0)
	class Meta           : unique_together = ('composant', 'version',)
	def __unicode__(self): return "%s : %s" % (self.composant, self.version)

class Client(models.Model):
	designation = models.CharField(max_length = 255)
	num_compte  = models.IntegerField()
	description = models.TextField()
	address     = models.TextField()
	def __unicode__(self): return self.designation

class Produit(models.Model):
	titre       = models.CharField(max_length = 255, unique = True)
	versions    = models.ManyToManyField(VersionLogiciel, through = 'ProduitVersion')
	description = models.TextField()
	def __unicode__(self): return self.titre

class ProduitVersion(models.Model):
	produit    = models.ForeignKey(Produit)
	version    = models.ForeignKey(VersionLogiciel)
	client     = models.ForeignKey(Client)
	etat       = models.ForeignKey(Etat)
	composants = models.ManyToManyField(ComposantVersion, through = 'ProduitVersionComposantVersion')
	class Meta            : unique_together = ('produit', 'version',)
	def __unicode__ (self): return "%s : %s" % (self.produit, self.version)
	def cout_nominal(self): return reduce(lambda x,y: x+y ,map(lambda x: x.cout, self.composants.all()), 0)

class ProduitVersionComposantVersion(models.Model):
	produit_version   = models.ForeignKey(ProduitVersion)
	composant_version = models.ForeignKey(ComposantVersion)
	class Meta            : unique_together = ('produit_version', 'composant_version',)
	def __unicode__(self) : return "%s -> %s" % (self.produit_version, self.composant_version)