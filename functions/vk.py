from nicegui import ui
from functions.crud import add_in_vault_keys

def vk_add_new_key(name, key, table, rows_hidden, rows_unhidden, logs):
    
    if not name.value or not key.value:
        
        logs.push('Failed to add new data because\nyou didnt filled all the fields.', classes = 'text-red')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        ui.notify(message='You need to complete all fields.', position = 'bottom', type = 'negative')
        
    else:
        
        new_id  = (max([r['id'] for r in rows_hidden], default=0) + 1) if rows_hidden else 1

        rows_hidden.append({'id': new_id, 'name': name.value, 'key': '*' * len(key.value)})
        rows_unhidden.append({'id': new_id, 'name': name.value, 'key': key.value})
        
        logs.push(line = f'New key added for name: {name.value}', classes = 'text-green')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        
        add_in_vault_keys(new_id, name.value, key.value)
        key.set_value(None)
        name.set_value(None)
        
        table.options['rowData'] = rows_hidden
        table.update()
        
        ui.notify(message = 'New account added.', position = 'bottom', type = 'positive')