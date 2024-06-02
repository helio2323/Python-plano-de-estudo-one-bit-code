from conexao_orm import Base, engine, session
from User import User
from Post import Post

Base.metadata.create_all(engine)

#Funcao para exibir o menu de opcoes

def show_menu():
    print('Menu de Opções:')
    print('1 - Cadastrar Usuário')
    print('2 - Cadastrar Post')
    print('3 - Consultar Usuários e seus Posts')
    print('4 - Sair')
    
#Funcao para cadastrar um novo usuario
def add_user():
     print('Cadastro de Usuário')
     name = input('Nome:\n ')
     email = input('Email:\n ')
     user = User(name, email)
     session.add(user)
     session.commit()
     print('Usário Cadastrado com sucesso!')
     
add_user()