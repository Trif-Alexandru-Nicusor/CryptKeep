from nicegui import ui
from components import navbar
from functions.vault_accounts import *

@ui.page('/vault_accounts')
def vault_accounts_page():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        with ui.row().classes('gap-24'):
            
            hide_unhide_password_button = ui.button(icon = 'visibility',
                                                    on_click = lambda: hide_unhide_password(table_accounts, rows_unhidden_password,hide_unhide_password_button, 
                                                                                            logs, type_filter_select, name_filter_input, email_id_username_filter_input))
            hide_unhide_password_button.tailwind.background_color('transparent')
            hide_unhide_password_button.tooltip(text = 'Hide or unhide the account or accounts selected. If you want to use the filters, you need to unhide or hide passwords first.')
            
            with ui.dialog() as dialog, ui.card():
                type_account_select = ui.select(label = 'Type', options = ['Site', 'App'], clearable = True)
                type_account_select.style('width: 150px;').props('outlined')
                
                name_app_site__input = ui.input(label = 'Name')
                name_app_site__input.style('width: 150px;').props('outlined')
                
                email_id_username_input = ui.input(label = 'Email/ID/Username')
                email_id_username_input.style('width: 150px;').props('outlined')
                
                password_account_input = ui.input(label = 'Password', password = True, password_toggle_button = True)
                password_account_input.style('width: 150px;').props('outlined')
                
                add_account_button = ui.button(text = 'Add Account', icon = 'person_add',
                                               on_click = lambda: add_new_account(type_account_select, name_app_site__input,email_id_username_input, password_account_input, 
                                                                                  table_accounts, rows_hidden_password, rows_unhidden_password, logs))
                add_account_button.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
            
            add_account_s_button = ui.button(icon = 'add', on_click = dialog.open)
            add_account_s_button.tailwind.background_color('transparent')
            add_account_s_button.tooltip(text = 'Add a account.')
            
            remove_account_s_butto = ui.button(icon = 'remove', on_click = lambda: remove_account_s(table_accounts, 
                                                                                                    rows_hidden_password, 
                                                                                                    rows_unhidden_password, 
                                                                                                    logs))
            remove_account_s_butto.tailwind.background_color('transparent')
            remove_account_s_butto.tooltip(text = 'Remove the account or accounts selected.')
            
            logs_vault_accounts_button = ui.button(icon = 'download')
            logs_vault_accounts_button.tailwind.background_color('transparent')
            logs_vault_accounts_button.tooltip(text = 'Download the account or accounts selected.')
            
            with ui.dialog() as dialog1, ui.card():
                logs = ui.log()
                logs.style('width: 500px')
            
            history_account_s_button = ui.button(icon = 'history', on_click = dialog1.open)
            history_account_s_button.tailwind.background_color('transparent')
            history_account_s_button.tooltip(text = 'See your last actions.')
        
        with ui.expansion(text = 'Filters', icon = 'filter_list').style('border: 1px solid #ccc; border-radius: 8px;'):
            with ui.row().classes('gap-20'):
                type_filter_select= ui.select(label = 'Type', options = ['Site', 'App'], clearable = True,
                                              on_change = lambda: filter_vault_accounts(type_filter_select, name_filter_input, email_id_username_filter_input, 
                                                                                        rows_hidden_password, rows_unhidden_password, table_accounts, 
                                                                                        hide_unhide_password_button.icon)).style('width: 150px;').props('outlined')
                
                name_filter_input = ui.input(label = 'Name',
                                             on_change = lambda: filter_vault_accounts(type_filter_select, name_filter_input, email_id_username_filter_input, 
                                                                                       rows_hidden_password, rows_unhidden_password, table_accounts, 
                                                                                       hide_unhide_password_button.icon)).style('width: 150px;').props('outlined')
                
                email_id_username_filter_input = ui.input(label = 'Email/ID/Username', 
                                                          on_change = lambda: filter_vault_accounts(type_filter_select, name_filter_input, email_id_username_filter_input, 
                                                                                                    rows_hidden_password, rows_unhidden_password, table_accounts, 
                                                                                                    hide_unhide_password_button.icon)).style('width: 150px;').props('outlined')
       
        columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'type', 'label': 'Type', 'field': 'type', 'align': 'center'},
            {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'center'},
            {'name': 'email_id_username', 'label': 'Email/ID/Username', 'field': 'email_id_username', 'align': 'center'},
            {'name': 'password', 'label': 'Password', 'field': 'password', 'align': 'center'},
        ]
        rows_hidden_password = []
        rows_unhidden_password = []
        table_accounts = ui.table(
            columns = columns,
            rows = rows_hidden_password,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')