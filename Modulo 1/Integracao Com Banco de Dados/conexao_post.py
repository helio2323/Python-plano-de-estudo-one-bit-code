import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="fliperama",
        user="postgres",
        password="postgres"
    )
    print("Conexão bem-sucedida!")
except psycopg2.OperationalError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")


