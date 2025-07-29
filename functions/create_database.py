import sqlite3

db_name = "cryptkeep.db"

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

tables_sql = [
    """
    CREATE TABLE IF NOT EXISTS vault_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        name TEXT,
        email_id_username TEXT,
        password TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS vault_cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        name_on_card TEXT,
        card_number TEXT,
        expiration_date TEXT,
        cvv TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS vault_keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        key TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS vault_personal_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        pin TEXT,
        document_number TEXT,
        date_of_issue TEXT,
        expiration_date TEXT,
        issuing_authority TEXT,
        date_of_birth TEXT,
        address TEXT
    );
    """
]
for sql in tables_sql:
    cursor.execute(sql)
conn.commit()
conn.close()

