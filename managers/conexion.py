import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
SUPABASE_CONN = os.getenv("SUPABASE_CONN")

def cursorxd():
    if not SUPABASE_CONN:
        raise ValueError("SUPABASE_CONN no encontrada")

    conn = psycopg.connect(SUPABASE_CONN, sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()
