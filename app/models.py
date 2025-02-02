from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    # Defining the schema
    id = Column(Integer, primary_key=True, index=True)
    time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    sensor_id = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)