from Cheetah.Template            import Template
from gestion.api.resources       import create_resources
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'generate resource classes'

    def handle(self, *args, **options):
        resources_map = create_resources()
        