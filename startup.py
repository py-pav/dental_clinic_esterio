import os

import django
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dental_clinic.settings')
django.setup()


def run_migrations():
    try:
        print("Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        print("Migrations completed successfully!")
    except Exception as e:
        print(f"Migration error: {e}")


if __name__ == "__main__":
    run_migrations()
