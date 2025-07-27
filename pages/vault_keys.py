from nicegui import ui
from components import navbar

@ui.page('/vault_keys')
def vault_keys_page():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        with ui.row().classes('gap-24'):
            
            vk_hide_unhide_button = ui.button(icon = 'visibility')
            vk_hide_unhide_button.tailwind.background_color('transparent')
            vk_hide_unhide_button.tooltip(text = 'Hide or unhide the key/s selected.')
            
            with ui.dialog() as dialog, ui.card():
                vk_name = ui.input(label = 'Name')
                vk_name.style('width: 150px;').props('outlined')
                
                vk_key_input = ui.input(label = 'Key')
                vk_key_input.style('width: 150px;').props('outlined')
                
                vk_add_key_button = ui.button(text = 'Add Key', icon = 'add')
                vk_add_key_button.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
                
            vk_add_key_s_button = ui.button(icon = 'add', on_click = dialog.open)
            vk_add_key_s_button.tailwind.background_color('transparent')
            vk_add_key_s_button.tooltip(text = 'Add a key.')
            
            vk_remove_key_s_button = ui.button(icon = 'remove')
            vk_remove_key_s_button.tailwind.background_color('transparent')
            vk_remove_key_s_button.tooltip(text = 'Remove the key/s selected.')
            
            vk_download_key_s_button = ui.button(icon = 'download')
            vk_download_key_s_button.tailwind.background_color('transparent')
            vk_download_key_s_button.tooltip(text = 'Download the key/s selected.')
            
            with ui.dialog() as dialog1, ui.card():
                vk_logs = ui.log()
                vk_logs.style('width: 500px')
                
            vk_logs_button = ui.button(icon = 'history', on_click = dialog1.open)
            vk_logs_button.tailwind.background_color('transparent')
            vk_logs_button.tooltip(text = 'See your last actions.')
            
        with ui.expansion(text = 'Filters', icon = 'filter_list').style('border: 1px solid #ccc; border-radius: 8px;'):
            with ui.row().classes('gap-20'):
                vk_name_filter_input= ui.input(label = 'Name').style('width: 150px;').props('outlined')
                vk_key_filter_input = ui.input(label = 'Key').style('width: 150px;').props('outlined')
                
        vk_columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'center'},
            {'name': 'key', 'label': 'Key', 'field': 'key', 'align': 'center'},
        ]
        vk_rows_hidden = []
        vk_rows_unhidden =[]
        table_keys = ui.table(
            columns = vk_columns,
            rows = vk_rows_hidden,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')