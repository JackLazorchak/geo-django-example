from django.core.management import BaseCommand
from world import load


class Command(BaseCommand):
    help = 'Load data into table'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('model_name', help='Name to populate')

    def handle(self, *args, **options):
        model_name = options.get('model_name')
        load.run(model_name=model_name)
