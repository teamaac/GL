from django.db import models

class AbstractInfo(models.Model):
    label       = models.SlugField(max_length=20, unique=True)
    description = models.TextField(                          )
    class Meta           : abstract = True
    def __unicode__(self): return self.label

class Etat           (AbstractInfo):pass
class Nature         (AbstractInfo):pass
class TypeComposant  (AbstractInfo):pass
class VersionLogiciel(AbstractInfo):pass

class Licence(models.Model):
    label    = models.SlugField   (max_length=20, unique=True)
    libre    = models.BooleanField(                          )
    gratuit  = models.BooleanField(                          )
    contenu  = models.TextField   (                          )
    def __unicode__(self): return self.label

class Composant(models.Model):
    titre          = models.SlugField      (max_length=20, unique=True                 )
    versions       = models.ManyToManyField(VersionLogiciel, through='ComposantVersion')
    description    = models.TextField      (                                           )
    type_composant = models.ForeignKey     (TypeComposant                              )
    def __unicode__(self): return self.titre

class ComposantVersion(models.Model):
    cout           = models.PositiveIntegerField(               )
    nature         = models.ForeignKey          (Nature         )
    licence        = models.ForeignKey          (Licence        )
    version        = models.ForeignKey          (VersionLogiciel)
    composant      = models.ForeignKey          (Composant      )
    class Meta           : unique_together = ('composant', 'version',)
    def __unicode__(self): return "%s : %s" % (self.composant, self.version)

class Client(models.Model):
    address        = models.TextField   (             )
    designation    = models.SlugField   (max_length=20)
    description    = models.TextField   (             )
    numero_compte  = models.IntegerField(             )
    def __unicode__(self): return self.designation

class Produit(models.Model):
    titre       = models.SlugField      (max_length=20, unique=True               )
    versions    = models.ManyToManyField(VersionLogiciel, through='ProduitVersion')
    description = models.TextField      (                                         )
    def __unicode__(self): return self.titre

class ProduitVersion(models.Model):
    etat       = models.ForeignKey     (Etat                                                      )
    client     = models.ForeignKey     (Client                                                    )
    produit    = models.ForeignKey     (Produit                                                   )
    version    = models.ForeignKey     (VersionLogiciel                                           )
    composants = models.ManyToManyField(ComposantVersion, through='ProduitVersionComposantVersion')
    class Meta            : unique_together = ('produit', 'version',)
    def __unicode__ (self): return "%s : %s" % (self.produit, self.version)
    def cout_nominal(self): return reduce(lambda x,y: x+y ,map(lambda x: x.cout, self.composants.all()), 0)

class ProduitVersionComposantVersion(models.Model):
    produit_version   = models.ForeignKey(ProduitVersion  )
    composant_version = models.ForeignKey(ComposantVersion)
    class Meta            : unique_together = ('produit_version', 'composant_version',)
    def __unicode__(self) : return "%s -> %s" % (self.produit_version, self.composant_version)