from jinja2 import Environment, PackageLoader
from gestion.api.resources       import create_resources
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'generate resource classes'

    def handle(self, *args, **options):
        data           = create_resources()
        environment    = Environment(loader=PackageLoader('gestion', 'management/commands'))
        template       = environment.get_template('resources.tpl')
        generated_data = template.render(
            resources_map = data.resources_map,
            models_module = data.models_module)
        print generated_data