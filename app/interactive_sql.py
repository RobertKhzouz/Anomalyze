from sqlalchemy.orm import Session
from database import get_db
from models import SensorData
from datetime import datetime, UTC

class Commands:
    """Helper class for common SQL queries on sensor_data."""

    @staticmethod
    def insert_sensor(sensor_id: str, temperature: float):
        """Insert a new sensor reading into the database."""
        with next(get_db()) as db:
            new_data = SensorData(
                sensor_id=sensor_id,
                temperature=temperature,
                time=datetime.now(UTC)
            )
            db.add(new_data)
            db.commit()
            print(f"✅ Inserted: {sensor_id} - Temp: {temperature}°C at {new_data.time}")

    @staticmethod
    def insert_bulk_sensors(sensor_readings: list):
        """Insert multiple sensor readings."""
        with next(get_db()) as db:
            bulk_data = [
                SensorData(sensor_id=sensor, temperature=temp, time=datetime.now(UTC))
                for sensor, temp in sensor_readings
            ]
            db.add_all(bulk_data)
            db.commit()
            print(f"✅ Inserted {len(sensor_readings)} sensor readings.")

    @staticmethod
    def fetch_all():
        """Retrieve all sensor readings."""
        with next(get_db()) as db:
            results = db.query(SensorData).order_by(SensorData.time.desc()).all()
            return results  # Returns a list of SensorData objects

    @staticmethod
    def fetch_latest(n=10):
        """Retrieve the latest N sensor readings."""
        with next(get_db()) as db:
            results = db.query(SensorData).order_by(SensorData.time.desc()).limit(n).all()
            return results

    @staticmethod
    def update_sensor_temperature(sensor_id: str, new_temperature: float):
        """Update the temperature of a specific sensor."""
        with next(get_db()) as db:
            sensor_record = db.query(SensorData).filter(SensorData.sensor_id == sensor_id).first()
            if sensor_record:
                print(f"🔍 Before Update: {sensor_record.sensor_id} - {sensor_record.temperature}°C")
                sensor_record.temperature = new_temperature
                db.commit()
                db.refresh(sensor_record)
                print(f"✅ Updated: {sensor_record.sensor_id} - {sensor_record.temperature}°C")
            else:
                print(f"⚠️ No record found for {sensor_id}")

    @staticmethod
    def delete_sensor(sensor_id: str):
        """Delete sensor data for a specific sensor_id."""
        with next(get_db()) as db:
            deleted_count = db.query(SensorData).filter(SensorData.sensor_id == sensor_id).delete()
            db.commit()
            if deleted_count:
                print(f"🗑️ Deleted {deleted_count} records for sensor: {sensor_id}")
            else:
                print(f"⚠️ No records found for sensor: {sensor_id}")

    @staticmethod
    def delete_all():
        """Delete all sensor data."""
        with next(get_db()) as db:
            deleted_count = db.query(SensorData).delete()
            db.commit()
            print(f"🗑️ Deleted all {deleted_count} sensor readings.")