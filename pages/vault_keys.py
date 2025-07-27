from nicegui import ui
from components import navbar

@ui.page('/vault_keys')
def vault_keys_page():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        with ui.row().classes('gap-24'):
            hide_unhide_keys_button = ui.button(icon = 'visibility')
            hide_unhide_keys_button.tailwind.background_color('transparent')
            hide_unhide_keys_button.tooltip(text = 'Hide or unhide the account or accounts selected. If you want to use the filters, you need to unhide or hide passwords first.')
            
            with ui.dialog() as dialog, ui.card():
                name_keys_input = ui.input(label = 'Name')
                name_keys_input.style('width: 150px;').props('outlined')
                key_input = ui.input(label = 'Key')
                key_input.style('width: 150px;').props('outlined')
                add_key_button = ui.button(text = 'Add Key', icon = 'add')
                add_key_button.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
                
            add_key_s_button = ui.button(icon = 'add', on_click = dialog.open)
            add_key_s_button.tailwind.background_color('transparent')
            add_key_s_button.tooltip(text = 'Add a account.')
            
            remove_key_s_button = ui.button(icon = 'remove')
            remove_key_s_button.tailwind.background_color('transparent')
            remove_key_s_button.tooltip(text = 'Remove the account or accounts selected.')
            
            download_key_s_button = ui.button(icon = 'download')
            download_key_s_button.tailwind.background_color('transparent')
            download_key_s_button.tooltip(text = 'Download the account or accounts selected.')
            
            with ui.dialog() as dialog1, ui.card():
                logs = ui.log()
                logs.style('width: 500px')
                
            logs_vault_keys = ui.button(icon = 'history', on_click = dialog1.open)
            logs_vault_keys.tailwind.background_color('transparent')
            logs_vault_keys.tooltip(text = 'See your last actions.')
            
        with ui.expansion(text = 'Filters', icon = 'filter_list').style('border: 1px solid #ccc; border-radius: 8px;'):
            with ui.row().classes('gap-20'):
                name_filter_input= ui.input(label = 'Name').style('width: 150px;').props('outlined')
                key_filter_input = ui.input(label = 'Key').style('width: 150px;').props('outlined')
                
        columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'center'},
            {'name': 'key', 'label': 'Key', 'field': 'key', 'align': 'center'},
        ]
        rows = []
        table_keys = ui.table(
            columns = columns,
            rows = rows,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')