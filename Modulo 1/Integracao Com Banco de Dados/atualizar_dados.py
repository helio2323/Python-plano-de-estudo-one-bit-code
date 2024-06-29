import sqlite3

# Atualizar os dados da tabela movies.db

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

name = input("Qual o nome do filme?\n")
score = int(input("Qual o novo score do filme?\n"))

data = cursor.execute("""
UPDATE movies SET score = ?
WHERE name = ?
""", (score, name))

for row in data:
    print(row)

print(connection.total_changes)

connection.commit()
connection.close()