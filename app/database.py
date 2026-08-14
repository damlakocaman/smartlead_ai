import sqlite3
from config import Config


def get_db():
    conn = sqlite3.connect(Config.DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(app):
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()


def lead_ekle(isim, telefon, mesaj):
    with get_db() as conn:
        cursor = conn.execute(
            """
            INSERT INTO leads (isim, telefon, mesaj)
            VALUES (?, ?, ?)
            """,
            (isim, telefon, mesaj)
        )
        conn.commit()

        return cursor.lastrowid


def tum_leadler():
    with get_db() as conn:
        rows = conn.execute(
            """
            SELECT *
            FROM leads
            ORDER BY id ASC    # ASC KÜÇÜKTEN BÜYÜĞE SIRALA DEMEK
            """
        ).fetchall()

        return [dict(row) for row in rows]