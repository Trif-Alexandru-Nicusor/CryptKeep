from nicegui import ui
from functions.crud import add_in_table



def vpd_add_new_data(full_name, pin, document_number, date_of_issue, expiration_date, issuing_authority, date_of_birth, address, table, rows_hidden, rows_unhidden, logs):
    
    if not full_name.value or not pin.value or not document_number.value or not date_of_issue.value or not expiration_date.value or not issuing_authority.value or not date_of_birth.value or not address.value:
        
        logs.push('Failed to add new data because\nyou didnt filled all the fields.', classes = 'text-red')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        ui.notify(message='You need to complete all fields.', position = 'bottom', type = 'negative')
        
    else:
        
        new_id  = (max([r['id'] for r in rows_hidden], default=0) + 1) if rows_hidden else 1
        
        rows_hidden.append({'id': new_id, 'full_name': full_name.value, 'pin': '*' * len(pin.value), 'document_number': '*' * len(document_number.value), 'date_of_issue': date_of_issue.value, 'expiration_date': expiration_date.value, 'issuing_authority': issuing_authority.value, 'date_of_birth': date_of_birth.value, 'address': address.value})
        rows_unhidden.append({'id': new_id, 'full_name': full_name.value, 'pin': pin.value, 'document_number': document_number.value, 'date_of_issue': date_of_issue.value, 'expiration_date': expiration_date.value, 'issuing_authority': issuing_authority.value, 'date_of_birth': date_of_birth.value, 'address': address.value})
        
        logs.push(f'New data added for full name: {full_name.value}.', classes = 'text-green')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        
        add_in_table(
            table_name='vault_personal_data',
            columns=['id', 'full_name', 'pin', 'document_number', 'date_of_issue', 'expiration_date', 'issuing_authority', 'date_of_birth', 'address'],
            values=(new_id, full_name.value, pin.value, document_number.value, date_of_issue.value, expiration_date.value, issuing_authority.value, date_of_birth.value, address.value)
        )
        
        full_name.set_value(None)
        pin.set_value(None)
        document_number.set_value(None)
        date_of_issue.set_value(None)
        expiration_date.set_value(None)
        issuing_authority.set_value(None)
        date_of_birth.set_value(None)
        address.set_value(None)
        
        table.options['rowData'] = rows_hidden
        table.update()
        ui.notify(message = 'New data added.', position = 'bottom', type= 'positive')
        
    