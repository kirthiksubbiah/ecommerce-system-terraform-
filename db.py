import mysql.connector

# AWS RDS MySQL connection details
host = "database-1.c38cueauyeoe.us-east-1.rds.amazonaws.com"
port = 3306
database = "ecommerce"
user = "admin"
password = "admin123"

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        return conn
    except Exception as e:
        print("❌ DB connection error:", e)
        return None
