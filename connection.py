import sqlite3

db = 'database.db'
create_table = """CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name text NOT NULL
);"""

try:
    with sqlite3.connect(db) as conn:
        print(f'Openned SQLite database with version {sqlite3.sqlite_version} successfully.')

        # create cursor
        cursor = conn.cursor()

        # execute statements
        cursor.execute(create_table)
        print('Table created successfully.')

        # commit changes
        conn.commit()
        
except sqlite3.OperationalError as e:
    print('Database error:', e)
