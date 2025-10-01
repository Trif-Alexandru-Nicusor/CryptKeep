import sqlite3

def get_connection(db_name = 'cryptkeep.db'):
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    return conn, cursor

def add_in_vault_accounts(type, name, email_id_username, password):
    
    conn, cursor = get_connection()
    cursor.execute('''
                   INSERT INTO vault_accounts (type, name, email_id_username, password) VALUES (?, ?, ?, ?)
                   ''', (type, name, email_id_username, password))
    conn.commit()
    conn.close()

def delete_records_global(record_id, table, db_name="cryptkeep.db"):
    
    conn, cursor = get_connection(db_name)
    query = f"DELETE FROM {table} WHERE id = ?"
    cursor.execute(query, (record_id,))
    conn.commit()
    conn.close()

