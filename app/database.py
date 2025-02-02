# Initialize TimescaleDB Connection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from models import Base
    Base.metadata.create_all(bind=engine)
    # Creating hypertable (need to connect to engine first)
    # Hypertable because timeseries data
    with engine.connect() as conn:
        try:
            conn.execute("SELECT create_hypertable('sensor_data', 'time', if_not_exists => TRUE);")
            print("YOU CREATED THE HYPERTABLE!")
        except Exception as e:
            print(f"YOU GOT AN ERROR BUB: {e}")