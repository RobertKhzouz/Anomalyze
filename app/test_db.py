from database import get_db

# Test DB connection
try:
    db = get_db()
    print("✅ Connected to TimescaleDB successfully!")
    db.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")