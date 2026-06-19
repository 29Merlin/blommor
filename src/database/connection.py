import os
import psycopg2

conn = psycopg2.connect(
    host="db",
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cur = conn.cursor()

conn.commit()