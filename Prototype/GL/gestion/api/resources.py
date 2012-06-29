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
        resource_name = 'client'

class ComposantResource(tastypie.resources.ModelResource):
    type_composant = tastypie.fields.ForeignKey('gestion.api.resources.TypeComposantResource', 'type_composant', full=True)
    versions = tastypie.fields.ToManyField('gestion.api.resources.VersionLogicielResource', 'versions', full=True)
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.Composant.objects.all()
        resource_name = 'composant'

class ComposantVersionResource(tastypie.resources.ModelResource):
    composant = tastypie.fields.ForeignKey('gestion.api.resources.ComposantResource', 'composant', full=True)
    licence = tastypie.fields.ForeignKey('gestion.api.resources.LicenceResource', 'licence', full=True)
    nature = tastypie.fields.ForeignKey('gestion.api.resources.NatureResource', 'nature', full=True)
    version = tastypie.fields.ForeignKey('gestion.api.resources.VersionLogicielResource', 'version', full=True)
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.ComposantVersion.objects.all()
        resource_name = 'composantversion'

class EtatResource(tastypie.resources.ModelResource):
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.Etat.objects.all()
        resource_name = 'etat'

class LicenceResource(tastypie.resources.ModelResource):
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.Licence.objects.all()
        resource_name = 'licence'

class NatureResource(tastypie.resources.ModelResource):
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.Nature.objects.all()
        resource_name = 'nature'

class ProduitResource(tastypie.resources.ModelResource):
    versions = tastypie.fields.ToManyField('gestion.api.resources.VersionLogicielResource', 'versions', full=True)
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.Produit.objects.all()
        resource_name = 'produit'

class ProduitVersionResource(tastypie.resources.ModelResource):
    client = tastypie.fields.ForeignKey('gestion.api.resources.ClientResource', 'client', full=True)
    etat = tastypie.fields.ForeignKey('gestion.api.resources.EtatResource', 'etat', full=True)
    produit = tastypie.fields.ForeignKey('gestion.api.resources.ProduitResource', 'produit', full=True)
    version = tastypie.fields.ForeignKey('gestion.api.resources.VersionLogicielResource', 'version', full=True)
    composants = tastypie.fields.ToManyField('gestion.api.resources.ComposantVersionResource', 'composants', full=True)
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.ProduitVersion.objects.all()
        resource_name = 'produitversion'

class ProduitVersionComposantVersionResource(tastypie.resources.ModelResource):
    composant_version = tastypie.fields.ForeignKey('gestion.api.resources.ComposantVersionResource', 'composant_version', full=True)
    produit_version = tastypie.fields.ForeignKey('gestion.api.resources.ProduitVersionResource', 'produit_version', full=True)
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.ProduitVersionComposantVersion.objects.all()
        resource_name = 'produitversioncomposantversion'

class TypeComposantResource(tastypie.resources.ModelResource):
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.TypeComposant.objects.all()
        resource_name = 'typecomposant'

class VersionLogicielResource(tastypie.resources.ModelResource):
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = gestion.models.VersionLogiciel.objects.all()
        resource_name = 'versionlogiciel'

resources_api = tastypie.api.Api(api_name=settings.API_NAME)
resources_api.register(ClientResource())
resources_api.register(ComposantResource())
resources_api.register(ComposantVersionResource())
resources_api.register(EtatResource())
resources_api.register(LicenceResource())
resources_api.register(NatureResource())
resources_api.register(ProduitResource())
resources_api.register(ProduitVersionResource())
resources_api.register(ProduitVersionComposantVersionResource())
resources_api.register(TypeComposantResource())
resources_api.register(VersionLogicielResource())
