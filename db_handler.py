import sqlite3
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from db_schema import Base, User, Post
from passlib.hash import pbkdf2_sha512
# add unix epoch time
import datetime
import random

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
    
    def add_post(self, title, content, tags, username, filename):
        user_id = self.get_user_by_username(username).id
        post_datetime = datetime.datetime.now()
        post = Post(title=title, content=content, tags=tags, datetime=post_datetime, rating=0, file_names=filename, user_id=user_id)
        self.session.add(post)
        self.session.commit()

    def get_tags(self, sorting, time):#sort can be by "new", "random", "top". When its "top" time can be "all", "hour", "day", "week", "month", "year"
        # Check for invalid values
        if sorting not in ["new", "random", "top"]:
            raise ValueError(f"Invalid value for sorting argument. Got {sorting}")
        if time not in ["all", "hour", "day", "week", "month", "year"]:
            raise ValueError(f"Invalid value for time argument. Got {time}")
        if sorting == "top":
            if time == "all":
                posts = self.session.query(Post).order_by(Post.rating.desc()).all()
            elif time == "hour":
                posts = self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(hours=1)).order_by(Post.rating.desc()).all()
            elif time == "day":
                posts = self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(days=1)).order_by(Post.rating.desc()).all()
            elif time == "week":
                posts = self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(weeks=1)).order_by(Post.rating.desc()).all()
            elif time == "month":
                posts = self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(days=30)).order_by(Post.rating.desc()).all()
            elif time == "year":
                posts = self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(days=365)).order_by(Post.rating.desc()).all()

            tags = []
            for post in posts:
                #split tags by comma
                tags += post.tags.split(",")
            #get all posts and count occurences of each tag
            posts = self.session.query(Post).all()
            tag_count = {}
            for post in posts:
                for tag in post.tags.split(","):
                    if tag in tag_count:
                        tag_count[tag] += 1
                    else:
                        tag_count[tag] = 1

            #sort by count
            tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
            #keep first 10 tags
            tag_count = tag_count[:8]
            return tag_count

        elif sorting == "new":
            #take ten posts and get their tags
            posts = self.session.query(Post).order_by(Post.datetime.desc()).limit(10).all()
            tags = []
            for post in posts:
                #split tags by comma
                tags += post.tags.split(",")
            #remove duplicates
            tags = list(set(tags))
            #keep first 10 tags
            tags = tags[:8]
            #get all posts and count occurences of each tag
            posts = self.session.query(Post).all()
            tag_count = {}
            for post in posts:
                for tag in post.tags.split(","):
                    if tag in tag_count:
                        tag_count[tag] += 1
                    else:
                        tag_count[tag] = 1

            #sort by the most recent
            tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
            return tag_count

        elif sorting == "random":
            #take all the post id and select 10 random ones
            posts = self.session.query(Post).all()
            post_ids = []
            for post in posts:
                post_ids.append(post.id)
            random.shuffle(post_ids)
            post_ids = post_ids[:8]
            #get all posts and count occurences of each tag
            posts = self.session.query(Post).all()
            tag_count = {}
            for post in posts:
                for tag in post.tags.split(","):
                    if tag in tag_count:
                        tag_count[tag] += 1
                    else:
                        tag_count[tag] = 1
            
            #sort by count
            tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
            #keep first 10 tags
            tag_count = tag_count[:8]
            return tag_count

    def get_post_by_id(self, post_id):
        return self.session.query(Post).filter_by(id=post_id).first()


    def get_posts(self, sorting, time):#sort can be by "new", "random", "top". When its "top" time can be "all", "hour", "day", "week", "month", "year"
        # Check for invalid values
        if sorting not in ["new", "random", "top"]:
            raise ValueError(f"Invalid value for sorting argument. Got {sorting}")
        if time not in ["all", "hour", "day", "week", "month", "year"]:
            raise ValueError(f"Invalid value for time argument. Got {time}")
        if sorting == "top":
            if time == "all":
                posts = self.session.query(Post).order_by(Post.rating.desc()).all()
            elif time == "hour":
                posts =  self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(hours=1)).order_by(Post.rating.desc()).all()
            elif time == "day":
                posts =  self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(days=1)).order_by(Post.rating.desc()).all()
            elif time == "week":
                posts =  self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(weeks=1)).order_by(Post.rating.desc()).all()
            elif time == "month":
                posts =  self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(days=30)).order_by(Post.rating.desc()).all()
            elif time == "year":
                posts =  self.session.query(Post).filter(Post.datetime > datetime.datetime.now() - datetime.timedelta(days=365)).order_by(Post.rating.desc()).all()
            return posts[:10]
        elif sorting == "new":
            posts = self.session.query(Post).order_by(Post.datetime.desc()).all()
            return posts[:10]
            
        elif sorting == "random":
            #get all posts
            posts = self.session.query(Post).all()
            #shuffle them
            random.shuffle(posts)
            #return first 10
            return posts[:10]

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

    def search_posts(self, query, sorting, time, quantity): #the query can be a title, tag, post id or content. sort can be by "new", "random", "top". When its "top" time can be "all", "hour", "day", "week", "month", "year"
        # Check for invalid values
        if sorting not in ["new", "random", "top"]:
            raise ValueError(f"Invalid value for sorting argument. Got {sorting}")
        if time not in ["all", "hour", "day", "week", "month", "year"]:
            raise ValueError(f"Invalid value for time argument. Got {time}")
        if sorting == "top":
            if time == "all":
                posts = self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query))).order_by(Post.rating.desc()).all()
            elif time == "hour":
                posts =  self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query)), Post.datetime > datetime.datetime.now() - datetime.timedelta(hours=1)).order_by(Post.rating.desc()).all()
            elif time == "day":
                posts =  self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query)), Post.datetime > datetime.datetime.now() - datetime.timedelta(days=1)).order_by(Post.rating.desc()).all()
            elif time == "week":
                posts =  self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query)), Post.datetime > datetime.datetime.now() - datetime.timedelta(weeks=1)).order_by(Post.rating.desc()).all()
            elif time == "month":
                posts =  self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query)), Post.datetime > datetime.datetime.now() - datetime.timedelta(days=30)).order_by(Post.rating.desc()).all()
            elif time == "year":
                posts =  self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query)), Post.datetime > datetime.datetime.now() - datetime.timedelta(days=365)).order_by(Post.rating.desc()).all()
            return posts[:quantity]

        elif sorting == "new":
            posts = self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query))).order_by(Post.datetime.desc()).all()
            return posts[:quantity]
        elif sorting == "random":
            #get all posts
            posts = self.session.query(Post).filter(or_(Post.title.contains(query), Post.tags.contains(query), Post.content.contains(query), Post.id.is_(query))).all()
            #shuffle them
            random.shuffle(posts)
            #return first 10
            return posts[:quantity]
    
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
    db = DatabaseHandler()
    print(db.get_tags("random", "all"))
    db.close()
