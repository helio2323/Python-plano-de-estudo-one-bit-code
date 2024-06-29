from conexao_post import conn

cursor = conn.cursor()

games = [
    ('Super Mario', 1990, 8.5),
    ('Zelda', 1986, 9.2),
    ('Donkey Kong', 1981, 9.0),
    ('Fifa 23', 2022, 9.8)
]

for game in games:
    cursor.execute("INSERT into game (name, year, score) VALUES (%s, %s, %s)",
    game)

conn.commit()
conn.close()