from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configurações de conexão com o banco de dados
user = 'root'
password = 'root'
host = 'localhost'
port = '5050'
database = 'blog'

# URI do banco de dados com a formatação correta
DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

