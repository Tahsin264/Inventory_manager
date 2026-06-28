from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db_url = db_url = "postgresql://postgres:Tahsin264%40@localhost:5432/Tahsin"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush = False, bind = engine)