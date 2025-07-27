from nicegui import ui
from datetime import datetime

def add_new_account(type, name, email_id_username, password, table, rows_hidden_password, rows_unhidden_password, logs):
    if not type.value or not name.value or not email_id_username.value or not password.value:
        logs.push('Failed to add new account because you didnt filled all the fields.', classes = 'text-red')
        return ui.notify(message='You need to complete all fields.', position='bottom', type='negative')
    else:
        new_id  = (max([r['id'] for r in rows_hidden_password], default=0) + 1) if rows_hidden_password else 1
        rows_hidden_password.append({'id': new_id, 'type': type.value, 'name': name.value, 'email_id_username': email_id_username.value, 'password': '*' * len(password.value)})
        rows_unhidden_password.append({'id': new_id, 'type': type.value, 'name': name.value, 'email_id_username': email_id_username.value, 'password': password.value})
        logs.push(f'New account added for {type.value}: {name.value}, Email/ID/Username: {email_id_username.value}.', classes = 'text-green')
        type.set_value(None)
        name.set_value(None)
        email_id_username.set_value(None)
        password.set_value(None)
        table.rows = rows_hidden_password
        table.update()
        return ui.notify(message = 'Account added.', position = 'bottom', type= 'positive')
    
def remove_account_s(table, rows_hidden_password, rows_unhidden_password, logs):
    if table.selected != []:
        ids_de_sters = [row['id'] for row in table.selected]
        rows_hidden_password[:] = [row for row in rows_hidden_password if row['id'] not in ids_de_sters]
        rows_unhidden_password[:] = [row for row in rows_unhidden_password if row['id'] not in ids_de_sters]
        table.rows = rows_hidden_password
        table.selected.clear()
        table.update()
        logs.push('Account/s removed.', classes = 'text-green')
        return ui.notify(message='Account/s removed.', position='bottom', type='positive')
    else:
        logs.push('You need to select at least 1 row to remove account/s', classes = 'text-red')
        return ui.notify(message='You need to select at least 1 row.', position='bottom', type='negative')
    
def build_table_rows(rows_unhidden_password, selected_rows, show_passwords):
    selected_ids = {r['id'] for r in selected_rows}
    new_rows = []
    for row in rows_unhidden_password:
        if row['id'] in selected_ids and show_passwords:
            new_rows.append(row.copy())
        else:
            masked_row = row.copy()
            masked_row['password'] = '*' * len(row['password'])
            new_rows.append(masked_row)
    return new_rows


show_passwords = False
def hide_unhide_password(table, rows_unhidden_password, hide_unhide_password_button, logs, type_filter, name_filter, email_id_username_filter):
    global show_passwords
    if hide_unhide_password_button.icon == 'visibility':
        hide_unhide_password_button.set_icon('visibility_off')
        logs.push('Passwords unhidden.', classes='text-grey')
    else:
        hide_unhide_password_button.set_icon('visibility')
        logs.push('Passwords hidden.', classes='text-grey')
    show_passwords = not show_passwords
    all_rows = build_table_rows(
        rows_unhidden_password,
        table.selected,
        show_passwords
    )
    type_val = type_filter.value or ''
    name_val = (name_filter.value or '').lower()
    email_val = (email_id_username_filter.value or '').lower()
    filtered = []
    for row in all_rows:
        if type_val and row['type'] != type_val:
            continue
        if name_val and name_val not in row['name'].lower():
            continue
        if email_val and email_val not in row['email_id_username'].lower():
            continue
        filtered.append(row)
    table.rows = filtered

        
def filter_vault_accounts(type, name, email_id_username, rows_hidden, rows_unhidden, table, hidden_unhidden):
    if hidden_unhidden == 'visibility_off':
        rows1 = rows_unhidden
    else:
        rows1 = rows_hidden
    type_val = type.value or ''
    name_val = name.value.lower() if name.value else ''
    email_val = email_id_username.value.lower() if email_id_username.value else ''
    filtered = []
    for row in rows1:
        if type_val and row['type'] != type_val:
            continue
        if name_val and name_val not in row['name'].lower():
            continue
        if email_val and email_val not in row['email_id_username'].lower():
            continue
        filtered.append(row)
    table.rows = filtered