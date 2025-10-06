from nicegui import ui
from components import navbar
from functions import vk, globals

@ui.page('/vault_keys')
def vault_keys_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%').style('font-family: Times New Roman'):
        
        ui.label('Vault Keys').style('font-size: 25px; align-self: center')
        
        with ui.row().style('align-self: center'):
            
            vk_hide_unhide_button = ui.button(icon = 'visibility', on_click = lambda: globals.global_hide_unhide_things(vk_hide_unhide_button, vk_rows_hidden, vk_rows_unhidden, vk_table, vk_logs, 'vk'))
            vk_hide_unhide_button.props('color=transparent')
            vk_hide_unhide_button.tooltip(text = 'Hide or unhide the key/s selected.')
            
            with ui.dialog() as dialog, ui.card().style('font-family: Times New Roman'):
                vk_name_input = ui.input(label = 'Name')
                vk_name_input.style('width: 150px;').props('outlined')
                
                vk_key_input = ui.input(label = 'Key')
                vk_key_input.style('width: 150px;').props('outlined')
                
                vk_add_key_button = ui.button(text = 'Add Key', icon = 'add', on_click = lambda: vk.vk_add_new_key(vk_name_input, vk_key_input, vk_table, vk_rows_hidden, vk_rows_unhidden, vk_logs))
                vk_add_key_button.props('flat color=white text-color=white').style('text-transform: none; align-self: center')
                
            vk_add_key_s_button = ui.button(icon = 'add', on_click = dialog.open)
            vk_add_key_s_button.props('color=transparent')
            vk_add_key_s_button.tooltip(text = 'Add a key.')
            
            vk_remove_key_s_button = ui.button(icon = 'remove', on_click = lambda: globals.global_remove_data_from_tables(vk_table, 'vk', vk_rows_hidden, vk_rows_unhidden, vk_logs))
            vk_remove_key_s_button.props('color=transparent')
            vk_remove_key_s_button.tooltip(text = 'Remove the key/s selected.')
            
            vk_download_key_s_button = ui.button(icon = 'download')
            vk_download_key_s_button.props('color=transparent')
            vk_download_key_s_button.tooltip(text = 'Download the key/s selected.')
            
            with ui.dialog() as dialog1, ui.card().style('font-family: Times New Roman'):
                vk_logs = ui.log()
                vk_logs.style('width: 500px')
                
            vk_logs_button = ui.button(icon = 'history', on_click = dialog1.open)
            vk_logs_button.props('color=transparent')
            vk_logs_button.tooltip(text = 'See your last actions.')
            
                
        vk_rows_hidden = []
        vk_rows_unhidden =[]

        
        vk_columns = [
            {'headerName': 'ID', 'field': 'id', 'filter': 'agTextColumnFilter', 'floatingFilter': True, 'headerCheckboxSelection': True, 'checkboxSelection': True},
            {'headerName': 'Name', 'field': 'name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Key', 'field': 'key', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
        ]
        
        vk_rows_hidden = []
        vk_rows_unhidden = []
        
        with ui.scroll_area().style('height: 435px'):
            vk_table = ui.aggrid(options = {'columnDefs': vk_columns, 'rowData': vk_rows_hidden, 'rowSelection': 'multiple', 'pagination': True,
                                             'enableCellTextSelection': True, 'clipboard': True,
                                             'paginationPageSize': 6, 'paginationPageSizeSelector': [6, 10, 15, 20, 25, 30, 35, 40, 45, 50]}, theme = "alpine")
            vk_table.style('min-width: 1000px; align-self: center; height: 400px')
            vk_table.props('data-ag-theme-mode=dark')