from nicegui import ui
from functions.crud import add_in_vault_accounts

def va_add_new_account(type, name, email_id_username, password, table, rows_hidden, rows_unhidden, logs):
    
    if not type.value or not name.value or not email_id_username.value or not password.value:
        

        logs.push('Failed to add new data because\nyou didnt filled all the fields.', classes = 'text-red')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        ui.notify(message='Failed to add new data because you didnt filled all the fields.', position = 'bottom', type = 'negative')
        
    else:
        
        new_id  = (max([r['id'] for r in rows_hidden], default=0) + 1) if rows_hidden else 1

        rows_hidden.append({'id': new_id, 'type': type.value, 'name': name.value, 'email_id_username': email_id_username.value, 'password': '*' * len(password.value)})
        rows_unhidden.append({'id': new_id, 'type': type.value, 'name': name.value, 'email_id_username': email_id_username.value, 'password': password.value})
        
        logs.push(line = f'New password added for[\ntype: {type.value}\nname: {name.value}\nemail/id/username: {email_id_username.value}]', classes = 'text-green')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        
        add_in_vault_accounts(new_id, type.value, name.value, email_id_username.value, password.value)
        
        type.set_value(None)
        name.set_value(None)
        email_id_username.set_value(None)
        password.set_value(None)
        
        table.options['rowData'] = rows_hidden
        table.update()
        
        ui.notify(message = 'New account added.', position = 'bottom', type = 'positive')