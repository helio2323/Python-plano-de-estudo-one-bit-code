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
     
def add_post():
     print('Cadastro de Post')
     title = input('Título:\n ')
     content = input('Conteúdo:\n ')
     user_id = int(input('ID do Usuário:\n '))
     user = session.query(User).filter_by(id=user_id).first()
     if user:
        post = Post(title, content, user_id)
        session.add(post)
        session.commit()
        print('Post Cadastrado com sucesso!')
     else:
        print('Usário não encontrado!')
        
        
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print('----------------------')
        print(f'Usuário: {user.name} - Email: {user.email}')

        posts = session.query(Post).filter_by(user_id=user.id).all()
        for post in posts:

            print(f'Título: {post.title} - Conteúdo: {post.content}')
            print('----------------------')
            

