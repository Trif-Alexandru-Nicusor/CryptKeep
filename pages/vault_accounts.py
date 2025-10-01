from nicegui import ui
from components import navbar
from functions import va, globals

@ui.page('/vault_accounts')
def vault_accounts_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%; font-family: Times New Roman'):
        
        ui.label('Vault Accounts').style('font-size: 25px; align-self: center')
        
        with ui.row().style('align-self: center'):
            
            va_hide_unhide_button = ui.button(icon = 'visibility', on_click = lambda: globals.global_hide_unhide_things(va_hide_unhide_button, va_rows_hidden, va_rows_unhidden, va_table, va_logs, 'va'))
            va_hide_unhide_button.tailwind.background_color('transparent')
            va_hide_unhide_button.tooltip(text = 'Hide or unhide the account/s selected.')
            
            with ui.dialog() as va_dialog, ui.card().style('font-family: Times New Roman'):
                va_type_account_select = ui.select(label = 'Type', options = ['Site', 'App'], clearable = True)
                va_type_account_select.style('width: 170px;').props('outlined')
                
                va_name_app_site__input = ui.input(label = 'Name')
                va_name_app_site__input.style('width: 170px;').props('outlined')
                
                va_email_id_username_input = ui.input(label = 'Email/ID/Username')
                va_email_id_username_input.style('width: 170px;').props('outlined')
                
                va_password_account_input = ui.input(label = 'Password', password = True, password_toggle_button = True)
                va_password_account_input.style('width: 170px;').props('outlined')
                
                va_add_account_button = ui.button(text = 'Add Account', icon = 'person_add', on_click = lambda: va.va_add_new_account(va_type_account_select, va_name_app_site__input, va_email_id_username_input,
                                                                                                                                      va_password_account_input, va_table, va_rows_hidden, va_rows_unhidden, va_logs))
                va_add_account_button.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
            
            va_add_account_s_button = ui.button(icon = 'add', on_click = va_dialog.open)
            va_add_account_s_button.tailwind.background_color('transparent')
            va_add_account_s_button.tooltip(text = 'Add a account.')
            
            va_remove_account_s_button = ui.button(icon = 'remove', on_click = lambda: globals.global_remove_data_from_tables(va_table, 'va', va_rows_hidden, va_rows_unhidden, va_logs))
            va_remove_account_s_button.tailwind.background_color('transparent')
            va_remove_account_s_button.tooltip(text = 'Remove the account/s selected.')
            
            va_logs_button = ui.button(icon = 'download')
            va_logs_button.tailwind.background_color('transparent')
            va_logs_button.tooltip(text = 'Download the account/s selected.')
            
            with ui.dialog() as va_dialog1, ui.card().style('font-family: Times New Roman'):
                va_logs = ui.log()
                va_logs.style('width: 500px')
            
            va_logs_button = ui.button(icon = 'history', on_click = va_dialog1.open)
            va_logs_button.tailwind.background_color('transparent')
            va_logs_button.tooltip(text = 'See your last actions.')
       
        va_columns = [
            {'headerName': 'ID', 'field': 'id', 'filter': 'agTextColumnFilter', 'floatingFilter': True, 'headerCheckboxSelection': True, 'checkboxSelection': True,},
            {'headerName': 'Type', 'field': 'type', 'filter': 'agTextColumnFilter', 'floatingFilter': True, 'headerClass': 'ag-center-align'},
            {'headerName': 'Name', 'field': 'name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Email/ID/Username', 'field': 'email_id_username', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Password', 'field': 'password', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
        ]
        
        va_rows_hidden = []
        va_rows_unhidden = []
        with ui.scroll_area().style('height: 435px;'):
            va_table = ui.aggrid(options = {'columnDefs': va_columns, 'rowData': va_rows_hidden, 'rowSelection': 'multiple', 'pagination': True,
                                             'enableCellTextSelection': True, 'clipboard': True,
                                             'paginationPageSize': 6, 'paginationPageSizeSelector': [6, 10, 15, 20, 25, 30, 35, 40, 45, 50]}, theme = "alpine-dark")
            va_table.style('min-width: 1000px; align-self:center; height: 400px;')
            