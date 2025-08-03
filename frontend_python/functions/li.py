from nicegui import ui, app
import sqlite3
from functions import  encrypted_password

def log_in(username, password):
    
    if not username.value or not password.value:
        return ui.notification(message = 'You need to complete all the fields.', position = 'center', type = 'negative')
    
    else:
        
        is_native = app.native.main_window
        mode = 'Native' if is_native else 'Web'
        
        if mode == 'Native':
            conn = sqlite3.connect('../cryptkeep.db')
            cursor = conn.cursor()
            
        cursor.execute('SELECT password FROM users_data WHERE username = ?', (username.value,))
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            return ui.notification(message='Username not found.', position='center', type='negative')
        
        db_password = result[0]
        print(encrypted_password.check_password(password.value, db_password))
        