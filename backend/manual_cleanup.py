
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def cleanup():
    with connection.cursor() as cursor:
        # 1. Drop Index
        try:
            print("Dropping index voucher_con_effecti_a6b7a2_idx...")
            cursor.execute("DROP INDEX `voucher_con_effecti_a6b7a2_idx` ON `voucher_configurations`")
            print("Success.")
        except Exception as e:
            print(f"Error dropping index: {e}")

        # 2. Drop Columns
        cols = ['effective_from', 'effective_to', 'update_customer_master']
        for col in cols:
            try:
                print(f"Dropping column {col}...")
                cursor.execute(f"ALTER TABLE `voucher_configurations` DROP COLUMN `{col}`")
                print("Success.")
            except Exception as e:
                print(f"Error dropping column {col}: {e}")

if __name__ == '__main__':
    cleanup()
