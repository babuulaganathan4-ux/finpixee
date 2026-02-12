
import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def fix_table():
    sql_statements = [
        """
        CREATE TABLE `voucher_configurations` (
            `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
            `tenant_id` varchar(36) NOT NULL, 
            `created_at` datetime(6) NULL, 
            `updated_at` datetime(6) NULL, 
            `voucher_type` varchar(50) NOT NULL, 
            `voucher_name` varchar(255) NOT NULL, 
            `enable_auto_numbering` bool NOT NULL, 
            `prefix` varchar(50) NULL, 
            `suffix` varchar(50) NULL, 
            `start_from` bigint UNSIGNED NOT NULL CHECK (`start_from` >= 0), 
            `current_number` bigint UNSIGNED NOT NULL CHECK (`current_number` >= 0), 
            `required_digits` integer NOT NULL, 
            `effective_from` date NOT NULL, 
            `effective_to` date NOT NULL, 
            `update_customer_master` bool NULL, 
            `include_from_existing_series_id` bigint NULL, 
            `is_active` bool NOT NULL
        );
        """,
        """
        ALTER TABLE `voucher_configurations` ADD CONSTRAINT `voucher_configurations_tenant_id_voucher_type_v_47364db1_uniq` UNIQUE (`tenant_id`, `voucher_type`, `voucher_name`, `effective_from`);
        """,
        """
        CREATE INDEX `voucher_configurations_tenant_id_6da514d7` ON `voucher_configurations` (`tenant_id`);
        """,
        """
        CREATE INDEX `voucher_con_tenant__142b94_idx` ON `voucher_configurations` (`tenant_id`, `voucher_type`);
        """,
        """
        CREATE INDEX `voucher_con_effecti_a6b7a2_idx` ON `voucher_configurations` (`effective_from`, `effective_to`);
        """
    ]

    with connection.cursor() as cursor:
        for sql in sql_statements:
            try:
                print(f"Executing: {sql[:50]}...")
                cursor.execute(sql)
                print("Success.")
            except Exception as e:
                print(f"Error executing SQL: {e}")

if __name__ == '__main__':
    fix_table()
