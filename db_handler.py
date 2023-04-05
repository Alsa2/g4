import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_schema import Base, User, Post
from passlib.hash import pbkdf2_sha512
# add unix epoch time
import datetime

def create_db():
    engine = create_engine('sqlite:///database.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    my_session = sessionmaker(bind=engine)
    print(Base.metadata.tables.keys())
    print(engine.connect())
    return None

class DatabaseHandler():
    def __init__(self) -> None:
        self.session = None
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close(self):
        self.session.close()

    def add_user(self, username, unhashed_password):
        user = User(username=username, password=pbkdf2_sha512.hash(unhashed_password))
        self.session.add(user)
        self.session.commit()

    def login(self, username, unhashed_password):
        user = self.session.query(User).filter_by(username=username).first()
        if user is None:
            return False
        else:
            return pbkdf2_sha512.verify(unhashed_password, user.password)
    
    def add_post(self, title, content, tags, username):
        user_id = self.get_user_by_username(username).id
        post_datetime = datetime.datetime.now()
        post = Post(title=title, content=content, tags=tags, datetime=post_datetime, rating=0, user_id=user_id)
        self.session.add(post)
        self.session.commit()

    def get_posts(self):
        return self.session.query(Post).all()

    def get_posts_by_user_id(self, post_id):
        return self.session.query(Post).filter_by(id=post_id).all()

    def get_user(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()
    
    def get_user_posts(self, user_id):
        return self.session.query(Post).filter_by(user_id=user_id).all()
    
    def get_user_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def get_users(self):
        return self.session.query(User).all()

    def search_posts(self, query):
        return self.session.query(Post).filter(Post.title.like('%' + query + '%')).all()
    
    def delete_post(self, post_id):
        post = self.session.query(Post).filter_by(id=post_id).first()
        self.session.delete(post)
        self.session.commit()

    def change_rating(self, post_id, rating):
        post = self.session.query(Post).filter_by(id=post_id).first()
        post.rating = rating
        self.session.commit()
    
    def change_password(self, user_id, old_unhashed_password, new_password):
        user = self.session.query(User).filter_by(id=user_id).first()
        if pbkdf2_sha512.verify(old_unhashed_password, user.password):
            user.password = pbkdf2_sha512.hash(new_password)
            self.session.commit()
            return True
        else:
            return False

    def delete_user(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        self.session.delete(user)
        self.session.commit()

if __name__ == '__main__':
    create_db()
