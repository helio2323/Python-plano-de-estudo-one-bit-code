from conexao_post import conn

cursor = conn.cursor()

sql = "DELETE FROM game WHERE id = %s"

cursor.execute(sql, (5,))


conn.commit()
conn.close()