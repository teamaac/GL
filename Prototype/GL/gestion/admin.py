from django.contrib    import admin
from gestion.models import *

admin.site.register( Etat                           )
admin.site.register( Nature                         )
admin.site.register( Client                         )
admin.site.register( Produit                        )
admin.site.register( Licence                        )
admin.site.register( Composant                      )
admin.site.register( TypeComposant                  )
admin.site.register( ProduitVersion                 )
admin.site.register( VersionLogiciel                )
admin.site.register( ComposantVersion               )
admin.site.register( ProduitVersionComposantVersion )