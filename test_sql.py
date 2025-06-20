from db import get_db_connection

try:
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        row = cursor.fetchone()
        print("✅ Connected to AWS RDS MySQL!")
        print(f"MySQL Version: {row[0]}")
    else:
        print("❌ Connection not established.")
except Exception as e:
    print("❌ Error during test:", e)
