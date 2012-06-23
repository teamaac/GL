from gestion.models import *
from django.contrib import admin

class ComposantVersionInline(admin.TabularInline):
	extra = 0
	model = ComposantVersion

class ProduitVersionInline(admin.TabularInline):
	extra = 0
	model = ProduitVersion

class ProduitVersionComposantVersionInline(admin.TabularInline):
	extra = 0
	model = ProduitVersionComposantVersion

class ProduitAdmin         (admin.ModelAdmin): inlines = [ProduitVersionInline  ,]
class ComposantAdmin       (admin.ModelAdmin): inlines = [ComposantVersionInline,]

class ProduitVersionAdmin  (admin.ModelAdmin):
	search_fields = ['produit__titre']
	list_filter   = ('produit', 'version', 'client', 'etat')
	list_display  = ('produit', 'version', 'client', 'etat', 'cout_nominal')
	inlines = [ProduitVersionComposantVersionInline,]

class ComposantVersionAdmin(admin.ModelAdmin):
	search_fields = ['composants__titre']
	list_filter   = ('composant', 'version', 'nature', 'licence', 'cout')
	list_display  = ('composant', 'version', 'nature', 'licence', 'cout')
	inlines = [ProduitVersionComposantVersionInline,]

admin.site.register( Etat                                   )
admin.site.register( Nature                                 )
admin.site.register( Client                                 )
admin.site.register( Licence                                )
admin.site.register( TypeComposant                          )
admin.site.register( VersionLogiciel                        )

admin.site.register( Produit         , ProduitAdmin         )
admin.site.register( Composant       , ComposantAdmin       )
admin.site.register( ProduitVersion  , ProduitVersionAdmin  )
admin.site.register( ComposantVersion, ComposantVersionAdmin)