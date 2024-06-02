import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

# Ler dados da tabela

data = cursor.execute("""
SELECT score, year, name FROM movies ORDER BY score desc  
""")

for row in data:
    print(row)

connection.close()