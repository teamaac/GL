from sys                         import modules
from jinja2                      import Environment, PackageLoader
from gestion.api.tools           import create_resources
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'generate resource classes'

    def handle(self, *args, **options):
        data           = create_resources()
        path           = modules[data.api_module].__path__[0]
        result_file    = open(path+'/resources.py', 'w')
        environment    = Environment(loader=PackageLoader('gestion', 'management/commands'))
        template       = environment.get_template('resources.tpl')
        generated_data = template.render(
            api_module    = data.api_module,
            resources_map = data.resources_map,
            models_module = data.models_module,)
        result_file.write(generated_data)
        result_file.close()