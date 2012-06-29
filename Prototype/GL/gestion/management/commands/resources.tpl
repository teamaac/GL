import tastypie
import settings
import tastypie.api
import tastypie.resources
import ${models_module}

#for $resource in $resources_map
class ${resource.resource_name}(tastypie.resources.ModelResource):
    #for $field in $resource.model_fields
    $field.fk_field = tastypie.fields.ForeignKey('gestion.api.res.$field.mapped_resource', '$field.fk_field', full=True)
    #end for
    def determine_format(self, request): 
        return "application/json" 
    class Meta:
        queryset      = ${models_module}.${resource.model_name}.objects.all()
        resource_name = '${resource.resource_name}'

#end for

api = tastypie.api.Api(api_name=settings.API_NAME)
#for $resource in $resources_map
api.register(${resource.resource_name}())
#end for