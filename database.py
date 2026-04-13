from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

db_url = "YOURS DB URL ID"
engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
