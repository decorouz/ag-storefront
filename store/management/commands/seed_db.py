import os
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help: str = "Populates the database with collections and products"

    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        print("Populating the database...Updated")
        file_path = os.path.join(current_dir, "seed.sql")
        sql = Path(file_path).read_text()

        with connection.cursor() as cursor:
            cursor.execute(sql)
