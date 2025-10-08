import sqlite3
from collections import defaultdict

def get_connection(db_name = 'cryptkeep.db'):
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    return conn, cursor

def delete_records_global(record_id, table, db_name="cryptkeep.db"):
    
    conn, cursor = get_connection(db_name)
    query = f"DELETE FROM {table} WHERE id = ?"
    cursor.execute(query, (record_id,))
    conn.commit()
    conn.close()

def add_in_table(table_name: str, columns: list, values: tuple):

    conn, cursor = get_connection()
    try:
        cols_str = ', '.join(columns)
        placeholders = ', '.join(['?'] * len(columns))
        cursor.execute(
            f'INSERT INTO {table_name} ({cols_str}) VALUES ({placeholders})',
            values
        )
        conn.commit()
    finally:
        conn.close()

    
def get_vault_values(table_name: str, columns: list, mask_columns: list = []):

    conn, cursor = get_connection()
    
    cols_str = ', '.join(columns)
    cursor.execute(f'SELECT {cols_str} FROM {table_name}')
    rows = cursor.fetchall()
    
    hidden_list = []
    unhidden_list = []
    
    for row in rows:
        row_dict = dict(zip(columns, row))
        
        hidden_row = {}
        for col in columns:
            if col in mask_columns:
                hidden_row[col] = '*' * len(str(row_dict[col]))
            else:
                hidden_row[col] = row_dict[col]
        hidden_list.append(hidden_row)
        
        unhidden_list.append(row_dict)
    
    conn.close()
    return hidden_list, unhidden_list

def find_duplicate_passwords(logs):
    conn, cur = get_connection()
    
    try:
        cur.execute("SELECT id, password FROM vault_accounts")
        rows = cur.fetchall()

        password_map = defaultdict(list)
        for row_id, password in rows:
            password_map[password].append(row_id)

        duplicates = {pwd: ids for pwd, ids in password_map.items() if len(ids) > 1}

        if not duplicates:
            logs.push("No duplicates found.")
            return

        messages = []
        for pwd, ids in duplicates.items():
            ids_str = ", ".join(map(str, ids))
            messages.append(f"The same password is found at ids: {ids_str}.")

        logs.push("\n".join(messages))

    finally:
        conn.close()

