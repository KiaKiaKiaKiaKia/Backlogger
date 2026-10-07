import sqlite3

db = 'database.db'

def createTable():
    try:
        with sqlite3.connect(db) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    complete INTEGER NOT NULL DEFAULT 0,
                    review TEXT
            );""")
            print('Table created successfully.')
    except sqlite3.OperationalError as e:
        print('Database error:', e)

def addGame(name, genre):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute("""
                INSERT INTO games (name, genre)
                VALUES (?,?)
            """, (name, genre))
            print('Game added successfully.')
    except sqlite3.OperationalError as e:
        print('Database error:', e)

def viewGame(game):
    try:
        with sqlite3.connect(db) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT name, genre, complete, review
                FROM games
                WHERE name = ?
            """, (game,))

            row = cursor.fetchone()
            if row:
                return dict(row)
            return 'Game not found.'

    except sqlite3.OperationalError as e:
        print('Database error:', e)

def viewAllGames():
    try:
        with sqlite3.connect(db) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("""
                SELECT name, genre, complete, review
                FROM games
            """)

            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    except sqlite3.OperationalError as e:
        print('Database error:', e)

def deleteGame(game):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute("""
                DELETE FROM games
                WHERE name = ?
            """, (game,))
            print('Game deleted successfully.')
    except sqlite3.OperationalError as e:
        print('Database error:', e)