from conexao_post import conn

cursor = conn.cursor()


sql = "UPDATE game SET score = %s WHERE id = %s"

cursor.execute(sql, (9.5, 1))

conn.commit()
conn.close()