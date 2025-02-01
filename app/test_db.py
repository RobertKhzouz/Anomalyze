from database import SessionLocal

# Test DB connection
try:
    db = SessionLocal()
    print("✅ Connected to TimescaleDB successfully!")
    db.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")