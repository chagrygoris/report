from sqlalchemy import Column, String, Integer, MetaData, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

Base = declarative_base()
Base.metadata = MetaData(naming_convention=convention)
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
    creator = Column(Integer, ForeignKey(User.id))
