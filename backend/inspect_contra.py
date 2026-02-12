
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def inspect_contra():
    with connection.cursor() as cursor:
        try:
            cursor.execute("SHOW CREATE TABLE master_voucher_contra")
            result = cursor.fetchone()
            print(result[1])
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    inspect_contra()
