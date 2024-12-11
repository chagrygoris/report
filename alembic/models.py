from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = "t_users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    registered_at = Column(DateTime)

class Playlist(Base):
    __tablename__ = 't_playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    genre = Column(String(50))
    creator = Column(Integer, ForeignKey('t_users.id'))
