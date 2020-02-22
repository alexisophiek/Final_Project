from config import *
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
# from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
import os


#create your database in pgadmin4 as twitter_data
db_string = f'postgresql://{pguser}:{pw}@localhost:5432/twitter_data'
# db = os.environ.get('DATABASE_URL')
# engine = create_engine(db)
engine = create_engine(db_string)
print('Loading Engine...')

Base = declarative_base()


# Defining Schema
class Main (Base):
        __tablename__ = 'twitter_feed'
        date = Column(TIMESTAMP)
        place = Column(String)
        user_id = Column(String, primary_key = true)
        text = Column(String)
        meta_data = Column(String)


Main.__table__.create(bind = engine, checkfirst = True)

Base.metadata.create_all(engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

Session=sessionmaker(bind = engine)

print('Loading Schema...')
print('Loading Complete.')
