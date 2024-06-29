import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE movies (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    year INTEGER NOT NULL,
    score REAL NOT NULL
    );""")

print(connection.total_changes)

connection.commit()
connection.close()