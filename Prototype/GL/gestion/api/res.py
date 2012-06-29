import tastypie
import settings
import tastypie.api
import tastypie.resources
import gestion.models

class ClientResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.Client.objects.all()
        resource_name = 'ClientResource'

class ComposantResource(tastypie.resources.ModelResource):
    type_composant = tastypie.fields.ForeignKey('gestion.api.res.TypeComposantResource', 'type_composant', full=True)
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.Composant.objects.all()
        resource_name = 'ComposantResource'

class ComposantVersionResource(tastypie.resources.ModelResource):
    composant = tastypie.fields.ForeignKey('gestion.api.res.ComposantResource', 'composant', full=True)
    licence = tastypie.fields.ForeignKey('gestion.api.res.LicenceResource', 'licence', full=True)
    nature = tastypie.fields.ForeignKey('gestion.api.res.NatureResource', 'nature', full=True)
    version = tastypie.fields.ForeignKey('gestion.api.res.VersionLogicielResource', 'version', full=True)
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.ComposantVersion.objects.all()
        resource_name = 'ComposantVersionResource'

class EtatResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.Etat.objects.all()
        resource_name = 'EtatResource'

class LicenceResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.Licence.objects.all()
        resource_name = 'LicenceResource'

class NatureResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.Nature.objects.all()
        resource_name = 'NatureResource'

class ProduitResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.Produit.objects.all()
        resource_name = 'ProduitResource'

class ProduitVersionResource(tastypie.resources.ModelResource):
    client = tastypie.fields.ForeignKey('gestion.api.res.ClientResource', 'client', full=True)
    etat = tastypie.fields.ForeignKey('gestion.api.res.EtatResource', 'etat', full=True)
    produit = tastypie.fields.ForeignKey('gestion.api.res.ProduitResource', 'produit', full=True)
    version = tastypie.fields.ForeignKey('gestion.api.res.VersionLogicielResource', 'version', full=True)
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.ProduitVersion.objects.all()
        resource_name = 'ProduitVersionResource'

class ProduitVersionComposantVersionResource(tastypie.resources.ModelResource):
    composant_version = tastypie.fields.ForeignKey('gestion.api.res.ComposantVersionResource', 'composant_version', full=True)
    produit_version = tastypie.fields.ForeignKey('gestion.api.res.ProduitVersionResource', 'produit_version', full=True)
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.ProduitVersionComposantVersion.objects.all()
        resource_name = 'ProduitVersionComposantVersionResource'

class TypeComposantResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.TypeComposant.objects.all()
        resource_name = 'TypeComposantResource'

class VersionLogicielResource(tastypie.resources.ModelResource):
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = gestion.models.VersionLogiciel.objects.all()
        resource_name = 'VersionLogicielResource'


api = tastypie.api.Api(api_name=settings.API_NAME)
api.register(ClientResource())
api.register(ComposantResource())
api.register(ComposantVersionResource())
api.register(EtatResource())
api.register(LicenceResource())
api.register(NatureResource())
api.register(ProduitResource())
api.register(ProduitVersionResource())
api.register(ProduitVersionComposantVersionResource())
api.register(TypeComposantResource())
api.register(VersionLogicielResource())
