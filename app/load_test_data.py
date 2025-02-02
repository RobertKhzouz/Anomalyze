from sqlalchemy import inspect
from database import init_db, get_db
from interactive_sql import Commands
import random

def ensure_db_initialized():
    """Check if the database is initialized before running commands."""
    with next(get_db()) as db:
        inspector = inspect(db.bind)
        if "sensor_data" not in inspector.get_table_names():
            print("🚀 Table missing! Initializing database...")
            init_db()
        else:
            print("✅ Database is already initialized.")

def load_test_data():
    table = Commands()

    try:
        for i in range(10000):
            table.insert_sensor(random.randint(1,10), i % 90, i % 100)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")