import sqlite3

# Remove dados de movie.db

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

name = input("Qual o nome do filme?\n")

cursor.execute("""
DELETE FROM movies
WHERE name = ?
""", (name,))

print(connection.total_changes)

connection.commit()
connection.close()