import psycopg2
from conexao_post import conn

cursor = conn.cursor()
cursor.execute("SELECT * FROM game")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()