import sqlite3

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

def add_in_vault_accounts(id, type, name, email_id_username, password):
    
    conn, cursor = get_connection()
    cursor.execute('''
                   INSERT INTO vault_accounts (id, type, name, email_id_username, password) VALUES (?, ?, ?, ?, ?)
                   ''', (id, type, name, email_id_username, password))
    conn.commit()
    conn.close()
    
def add_in_vault_keys(id, name, key):
    
    conn, cursor = get_connection()
    cursor.execute('''
                   INSERT INTO vault_keys (id, name, key) VALUES (?, ?, ?)
                   ''', (id, name, key))
    conn.commit()
    conn.close()

def add_in_vault_cards(id, type, bank, cardholders_name, card_number, cvv, expiration_date):
    
    conn, cursor = get_connection()
    cursor.execute('''
                   INSERT INTO vault_cards (id, type, bank, cardholders_name, card_number, cvv, expiration_date) VALUES (?, ?, ?, ?, ?, ?, ?)
                   ''', (id, type, bank, cardholders_name, card_number, cvv, expiration_date))
    conn.commit()
    conn.close()
    
def add_in_vault_personal_data(id, full_name, pin, document_number, date_of_issue, expiration_date, issuing_authority, date_of_birth, address):
    
    conn, cursor = get_connection()
    cursor.execute('''
                   INSERT INTO vault_personal_data (id, full_name, pin, document_number, date_of_issue, expiration_date, issuing_authority, date_of_birth, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ''', (id, full_name, pin, document_number, date_of_issue, expiration_date, issuing_authority, date_of_birth, address))
    conn.commit()
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
        
        # hidden
        hidden_row = {}
        for col in columns:
            if col in mask_columns:
                hidden_row[col] = '*' * len(str(row_dict[col]))
            else:
                hidden_row[col] = row_dict[col]
        hidden_list.append(hidden_row)
        
        # unhidden
        unhidden_list.append(row_dict)
    
    conn.close()
    return hidden_list, unhidden_list
