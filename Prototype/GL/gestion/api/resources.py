import sys
import inspect
import tastypie
import settings
import collections
import tastypie.api
import gestion.tools
import tastypie.resources

def create_resources(models_module=settings.MODELS_MODULE):
    result         = collections.namedtuple('result'      , ['models_module', 'resources_map'                ])
    model_fields   = collections.namedtuple('model_fields', ['fk_field'     , 'mapped_resource'              ])
    resources_map  = collections.namedtuple('resource_map', ['resource_name', 'model_fields'   , 'model_name'])
    res = result(models_module = models_module.__name__, resources_map = [])
    for model in gestion.tools.nonabstract_models(models_module):
        tmp_resource_fields = []
        for field in gestion.tools.foreignkey_fields(model[1]):
            tmp_resource_fields.append(model_fields(
                fk_field        = field[0],
                mapped_resource = field[1].__name__+'Resource'))
        res.resources_map.append(resources_map(
            model_name    = model[1].__name__,
            resource_name = model[1].__name__+'Resource',
            model_fields  = tmp_resource_fields))
    return res

def register_resources(api_name, resources_map, resources_module=settings.RESOURCES_MODULE):
    api = tastypie.api.Api(api_name=api_name)
    for resource in resources_map:
        api.register(resource[0]())
    return api