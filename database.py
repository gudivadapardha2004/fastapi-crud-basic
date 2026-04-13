from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

db_url = "mysql+pymysql://root:pardha%40123@localhost:3306/users"
engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()