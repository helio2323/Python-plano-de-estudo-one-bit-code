from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from conexao_orm import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id
