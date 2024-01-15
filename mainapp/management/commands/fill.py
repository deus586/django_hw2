from django.core.management import BaseCommand, call_command

import os

from django.db import ProgrammingError, IntegrityError

from config.settings import BASE_DIR
from mainapp.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        fixture_path = os.path.join(BASE_DIR, 'fixtures', 'data.json')

        try:
            call_command('loaddata', fixture_path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write('OK', self.style.SUCCESS)
