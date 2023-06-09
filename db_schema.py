from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# crate a table user and table post

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = Column(String, default='user')
    posts = relationship("Post", backref="user")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    tags = Column(String)
    datetime = Column(String)
    rating = Column(Integer)
    file_names = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))