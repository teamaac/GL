import sys
import inspect
import tastypie
import settings
import tastypie.api
import gestion.tools
import tastypie.resources

resources_map  = []

def create_resources(models_module=settings.MODELS_MODULE, resource_module=settings.RESOURCES_MODULE):
    for model in gestion.tools.nonabstract_models(models_module):
        class Template(tastypie.resources.ModelResource):
            def determine_format(self, request): 
                return "application/json" 
            class Meta:
                queryset             = model[1].objects.all()
                resource_name        = model[1].__name__
        Template.__name__ = model[1].__name__+"Resource"
        resources_map.append((Template, model[1]))
        setattr(resource_module, Template.__name__, Template)

    for model in gestion.tools.nonabstract_models(models_module):
        for field in gestion.tools.foreignkey_fields(model[1]):
            for resource in resources_map:
                if resource[1] == field[1]:
                    for i in resources_map:
                        if i[1] == model[1]:
                            reverse_model = i[0]
                            break
                    setattr(reverse_model, field[0], tastypie.fields.ForeignKey(resource[0], field[0], full=True))

def register_resources(api_name, resources_module=settings.RESOURCES_MODULE):
    api = tastypie.api.Api(api_name=api_name)
    for resource in resources_map:
        api.register(resource[0]())
    return api

create_resources()
api = register_resources(settings.API_NAME)

