import sys
import inspect
import tastypie
import settings
import collections
import tastypie.api
import gestion.tools
import tastypie.resources

def create_resources(models_module=settings.MODELS_MODULE):
    data          = collections.namedtuple('data'        , ['models_module', 'resources_map'  ])
    model_fields  = collections.namedtuple('model_fields', ['field'        , 'mapped_resource'])
    resources_map = collections.namedtuple('resource_map', [
        'model_name'     ,
        'full_reverse'   ,
        'resource_name'  ,
        'resource_class' ,
        'fk_model_fields',
        'mm_model_fields',])
    result = data(models_module = models_module.__name__, resources_map = [])
    for model in gestion.tools.nonabstract_models(models_module):
        tmp_fk_resource_fields = []
        tmp_mm_resource_fields = []
        for field in gestion.tools.foreignkey_fields(model[1]):
            tmp_fk_resource_fields.append(model_fields(field=field[0], mapped_resource=field[1].__name__+'Resource'))
        for field in gestion.tools.many_to_many_fields(model[1]):
            tmp_mm_resource_fields.append(model_fields(field=field[0], mapped_resource=field[1].__name__+'Resource'))
        result.resources_map.append(resources_map(
            model_name      = model[1].__name__,
            full_reverse    = True,
            resource_name   = model[1].__name__.lower(),
            resource_class  = model[1].__name__+'Resource',
            fk_model_fields = tmp_fk_resource_fields,
            mm_model_fields = tmp_mm_resource_fields))
    return result