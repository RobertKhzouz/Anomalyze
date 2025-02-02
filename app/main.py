import random
from datetime import datetime, UTC
import uuid
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import SensorData, Base
from config import DATABASE_URL
from database import get_db, init_db

# Function to insert sensor data
def insert_sensor_data(db: Session):
    sensor_id = f"sensor_{random.randint(1, 5)}"
    temperature = round(random.uniform(20.0, 30.0), 2)  # Random temp between 20-30°C
    timestamp = datetime.now(UTC)
    
    # Create new sensor reading
    new_data = SensorData(
        sensor_id=sensor_id, 
        temperature=temperature, 
        time=timestamp
    )
    db.add(new_data)
    db.commit()
    print(f"✅ Inserted: {sensor_id} - Temp: {temperature}°C at {timestamp}")

# Bulk insert multiple records
def insert_bulk_data(db: Session, n=10):
    bulk_data = []
    for _ in range(n):
        sensor_id = f"sensor_{random.randint(1, 5)}"
        timestamp = datetime.now(UTC)
        temperature = round(random.uniform(20.0, 30.0), 2)
        
        bulk_data.append(SensorData(
            sensor_id=sensor_id,
            temperature=temperature,
            time=timestamp
        ))
    
    db.add_all(bulk_data)
    db.commit()
    print(f"✅ Inserted {n} sensor readings!")

# Run the script
if __name__ == "__main__":
    print("🚀 Loading data into TimescaleDB...")
    init_db()
    
    # Get database session
    db = next(get_db())
    
    try:
        # Insert single record
        insert_sensor_data(db)
        
        # Insert bulk records
        insert_bulk_data(db, 10)  # Insert 10 records
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        db.close()