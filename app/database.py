from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()  

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not set in .env")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


<<<<<<< HEAD
#mainbranch
try:
    with engine.connect() as conn:
        print("Successfully connected to the database!")
except Exception as e:
    print("Database connection failed!")
=======
try:
    with engine.connect() as conn:
        print("Successfully connected to the database!hiiiiiiiiiiiiiiiiiiiiiiiiii")
except Exception as e:
    print("Database connection failed!!!!!!!!!!!!!!!!!!!!")
>>>>>>> ccbaf6f6cf9ec06fccbad714dc5d663cbe5ee98d
    print(e)
