from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.sql import func
from database import Base, engine

class SensorData(Base):
    __tablename__ = "sensor_data"

    # Defining the schema
    id = Column(Integer, primary_key=True, index=True)
    time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    sensor_id = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)

# Creating hypertable (need to connect to engine first)
# Hypertable because timeseries data
with engine.connect() as conn:
    conn.execute("SELECT create_hypertable('sensor_data', 'time', if_not_exists => TRUE);")