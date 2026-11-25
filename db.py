from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://training_pyg7_user:aCp3bmObZM7EyMO884bufVis37Ng4QtP@dpg-dc35csjrjlhs73er237g-a.ohio-postgres.render.com/training_pyg7"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()


# def get_connection():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close