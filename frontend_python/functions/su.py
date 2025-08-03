from nicegui import ui, app
import sqlite3
from datetime import datetime
from functions import encrypted_password

def add_sign_up_data_to_db(first_name, last_name, username, email, password):
    
    if not first_name.value or not last_name.value or not username.value or not email.value or not password.value:
        return ui.notification(message = 'You need to complete all the fields.', position = 'center', type = 'negative')
    
    else:
        is_native = app.native.main_window
        mode = 'Native' if is_native else 'Web'
        
        if mode == 'Native':
            
            conn = sqlite3.connect('../cryptkeep.db')
            cursor = conn.cursor()
            
            cursor.execute('SELECT 1 FROM users_data WHERE username = ?', (username.value,))
            exists = cursor.fetchone()
            
            if exists:
                conn.close()
                return ui.notification(message='Username already exists!', position='center', type='negative')
            
            cursor.execute('''
                            INSERT INTO users_data (first_name, last_name, username, email, password, creation_date, is_active) VALUES (?, ?, ?, ?, ?, ?, ?)
                        ''', (first_name.value, last_name.value, username.value, email.value, encrypted_password.encrypt_password(password.value), datetime.now().strftime('%H:%M %d/%m/%Y'), 'Active'))
            conn.commit()
            conn.close()
            
            first_name.set_value(None)
            last_name.set_value(None)
            username.set_value(None)
            email.set_value(None)
            password.set_value(None)
            
            return ui.notification(message = 'Account created !', position = 'center', type = 'positive')
        else:
            pass