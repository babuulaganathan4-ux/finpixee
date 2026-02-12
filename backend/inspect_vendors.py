
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def inspect_vendors():
    with connection.cursor() as cursor:
        try:
            cursor.execute("SHOW TABLES LIKE 'vendor_%'")
            result = cursor.fetchall()
            print("Existing tables:")
            for row in result:
                print(row[0])
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    inspect_vendors()
