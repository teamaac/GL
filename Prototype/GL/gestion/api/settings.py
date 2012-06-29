import sys
import gestion.models

API_NAME              = "model"
MODELS_MODULE         = gestion.models
RESOURCES_MODULE_NAME = sys.modules[globals()['__name__']].__package__