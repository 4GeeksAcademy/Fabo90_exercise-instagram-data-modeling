import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False, unique=False)
    email = Column(String(60), nullable=False, unique=True)
    name = Column(String(30), nullable=False, unique=False)
    last_name = Column(String(30), nullable=False, unique=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    followed = Column(Integer, nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='followers')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False, unique=False)
    likes = Column(Integer, nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey ('user.id'))
    user = relationship('User', back_populates='post')

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='comments')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
