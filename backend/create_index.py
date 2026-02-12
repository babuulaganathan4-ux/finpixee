
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def create_index():
    sql = "CREATE INDEX `voucher_con_effecti_a6b7a2_idx` ON `voucher_configurations` (`effective_from`, `effective_to`)"
    with connection.cursor() as cursor:
        try:
            print(f"Executing: {sql}")
            cursor.execute(sql)
            print("Success.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    create_index()
