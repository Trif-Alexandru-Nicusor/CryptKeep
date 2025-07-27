from nicegui import ui
from components import navbar

@ui.page('/vault_accounts')
def vault_accounts_page():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        with ui.row().classes('gap-24'):
            
            va_hide_unhide_button = ui.button(icon = 'visibility')
            va_hide_unhide_button.tailwind.background_color('transparent')
            va_hide_unhide_button.tooltip(text = 'Hide or unhide the account/s selected.')
            
            with ui.dialog() as va_dialog, ui.card():
                va_type_account_select = ui.select(label = 'Type', options = ['Site', 'App'], clearable = True)
                va_type_account_select.style('width: 150px;').props('outlined')
                
                va_name_app_site__input = ui.input(label = 'Name')
                va_name_app_site__input.style('width: 150px;').props('outlined')
                
                va_email_id_username_input = ui.input(label = 'Email/ID/Username')
                va_email_id_username_input.style('width: 150px;').props('outlined')
                
                va_password_account_input = ui.input(label = 'Password', password = True, password_toggle_button = True)
                va_password_account_input.style('width: 150px;').props('outlined')
                
                va_add_account_button = ui.button(text = 'Add Account', icon = 'person_add')
                va_add_account_button.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
            
            va_add_account_s_button = ui.button(icon = 'add', on_click = va_dialog.open)
            va_add_account_s_button.tailwind.background_color('transparent')
            va_add_account_s_button.tooltip(text = 'Add a account.')
            
            va_remove_account_s_button = ui.button(icon = 'remove')
            va_remove_account_s_button.tailwind.background_color('transparent')
            va_remove_account_s_button.tooltip(text = 'Remove the account/s selected.')
            
            va_logs_button = ui.button(icon = 'download')
            va_logs_button.tailwind.background_color('transparent')
            va_logs_button.tooltip(text = 'Download the account/s selected.')
            
            with ui.dialog() as va_dialog1, ui.card():
                va_logs = ui.log()
                va_logs.style('width: 500px')
            
            va_logs_button = ui.button(icon = 'history', on_click = va_dialog1.open)
            va_logs_button.tailwind.background_color('transparent')
            va_logs_button.tooltip(text = 'See your last actions.')
        
        with ui.expansion(text = 'Filters', icon = 'filter_list').style('border: 1px solid #ccc; border-radius: 8px;'):
            with ui.row().classes('gap-20'):
                va_type_filter_select = ui.select(label = 'Type', options = ['Site', 'App'], clearable = True).style('width: 150px;').props('outlined')
                
                va_name_filter_input = ui.input(label = 'Name').style('width: 150px;').props('outlined')
                
                va_email_id_username_filter_input = ui.input(label = 'Email/ID/Username').style('width: 150px;').props('outlined')
       
        va_columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'type', 'label': 'Type', 'field': 'type', 'align': 'center'},
            {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'center'},
            {'name': 'email_id_username', 'label': 'Email/ID/Username', 'field': 'email_id_username', 'align': 'center'},
            {'name': 'password', 'label': 'Password', 'field': 'password', 'align': 'center'},
        ]
        
        va_rows_hidden = []
        va_rows_unhidden = []
        
        va_table = ui.table(
            columns = va_columns,
            rows = va_rows_hidden,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')