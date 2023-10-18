from matplotlib.pyplot import cla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, ForeignKey, Enum
import datetime
import enum
meta = MetaData()
Base = declarative_base()

class StatusEnum(enum.Enum):
    know = 1
    learn = 2

class LanguagsEnum(enum.Enum):
    en = 1
    ru = 2
    uz = 3
    
class UsersTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    telegram_id = Column(Integer, unique=True)
    word_learn = Column(Enum(LanguagsEnum))
    word_translate = Column(Enum(LanguagsEnum))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)


class WordsTable(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    word_en = Column(String)
    word_ru = Column(String)
    word_uz = Column(String)
    photo = Column(String, nullable=True)
    audio = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)




class UsersWordsTable(Base):
    __tablename__ = 'users_words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word_id = Column(Integer, ForeignKey('words.id'))
    status = Column(Enum(StatusEnum))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)
