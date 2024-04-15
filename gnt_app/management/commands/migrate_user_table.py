from django.core.management.base import BaseCommand
from django.db import connections, IntegrityError

from gnt_app.models import Members, Tbl_member


class Command(BaseCommand):
    help = 'Migrate tbl_user from MySQL to PostgreSQL'

    def handle(self, *args, **options):
        # Define your database aliases
        db_from = 'mysql'  # Source database
        db_to = 'default'  # Target database

        # Get the cursor for both databases
        cursor_from = connections[db_from].cursor()
        cursor_to = connections[db_to].cursor()

        try:
            # Explicitly name the columns to ensure correct data mapping
            cursor_from.execute('''
                SELECT 
                    id, 
                    username, 
                    email, 
                    password_hash, 
                    auth_key, 
                    access_token, 
                    logged_at, 
                    created_at, 
                    updated_at, 
                    isNewUser AS is_new_user,  # Aliasing MySQL column to match PostgreSQL
                    block_version, 
                    acceptedTermsId AS accepted_terms_id,  # Aliasing MySQL column to match PostgreSQL
                    acceptedTermsDate AS accepted_terms_date,  # Aliasing MySQL column to match PostgreSQL
                    isDeleted AS is_deleted  # Aliasing MySQL column to match PostgreSQL
                FROM tbl_user
            ''')
            rows = cursor_from.fetchall()

            # Define the SQL INSERT statement for PostgreSQL
            insert_query = '''
                INSERT INTO tbl_user 
                (id, username, email, password_hash, auth_key, access_token, logged_at, 
                 created_at, updated_at, is_new_user, block_version, accepted_terms_id, 
                 accepted_terms_date, is_deleted)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            # Insert data into PostgreSQL
            for row in rows:
                prepared_row = list(row)
                prepared_row[9] = bool(prepared_row[9])
                prepared_row[13] = bool(prepared_row[13])


                cursor_to.execute(insert_query, prepared_row)

            # Commit changes in PostgreSQL
            connections[db_to].commit()
            self.stdout.write(self.style.SUCCESS('Successfully migrated tbl_user from MySQL to PostgreSQL.'))
        except IntegrityError as e:
            # Handle specific errors related to data integrity
            self.stdout.write(self.style.ERROR(f'Integrity error: {e}'))
            connections[db_to].rollback()
        except Exception as e:
            # Handle any other exceptions
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
            connections[db_to].rollback()
        finally:
            # Close all cursors and databases to free up connections
            cursor_from.close()
            cursor_to.close()
            connections[db_from].close()
            connections[db_to].close()
