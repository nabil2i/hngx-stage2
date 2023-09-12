import os
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'create the database'

    def handle(self, *args, **options):
        print('Creating the database...')
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'hngx2_dump.sql')
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            cursor.execute(sql)
