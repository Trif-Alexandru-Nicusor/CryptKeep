from nicegui import ui
from components import navbar
from functions import vpd, globals

@ui.page('/vault_personal_data')
def vault_personal_data():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        
        with ui.row().classes('gap-20'):
            vpd_hide_unhide_pin_dn_button = ui.button(icon = 'visibility', on_click = lambda: vpd.vk_hide_unhide_cn_vcc(vpd_hide_unhide_pin_dn_button, vpd_rows_hidden, vpd_rows_unhidden, vpd_table, vpd_logs))
            vpd_hide_unhide_pin_dn_button.tailwind.background_color('transparent')
            vpd_hide_unhide_pin_dn_button.tooltip(text = 'Hide or unhide Identity Number and Document Number of selected data/s.')
            
            with ui.dialog() as vpd_dialog, ui.card():
                vpd_full_name_input = ui.input(label = 'Full Name')
                vpd_full_name_input.style('width: 200px;').props('outlined')
                
                
                vpd_pin_input = ui.input(label = 'PIN')
                vpd_pin_input.style('width: 200px;').props('outlined')
                
                vpd_document_number_input = ui.input(label = 'Document Number')
                vpd_document_number_input.style('width: 200px;').props('outlined')
                
                
                with ui.input('Date of Issue') as vpd_date_of_issue_input:
                    vpd_date_of_issue_input.style('width: 200px;').props('outlined')
                    with ui.menu().props('no-parent-event') as menu:
                        with ui.date(mask = 'DD/MM/YYYY').bind_value(vpd_date_of_issue_input):
                            with ui.row().classes('justify-end'):
                                ui.button('Close', on_click=menu.close).props('flat')
                    with vpd_date_of_issue_input.add_slot('append'):
                        ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
                        
                with ui.input('Expiration Date') as vpd_expiration_date_input:
                    vpd_expiration_date_input.style('width: 200px;').props('outlined')
                    with ui.menu().props('no-parent-event') as menu2:
                        with ui.date(mask = 'DD/MM/YYYY').bind_value(vpd_expiration_date_input):
                            with ui.row().classes('justify-end'):
                                ui.button('Close', on_click=menu2.close).props('flat')
                    with vpd_expiration_date_input.add_slot('append'):
                        ui.icon('edit_calendar').on('click', menu2.open).classes('cursor-pointer')
                        
                
                vpd_issuing_authority_input = ui.input(label = 'Issuing Authority')
                vpd_issuing_authority_input.style('width: 200px;').props('outlined')
                
                with ui.input('Date Of Birth') as vpd_date_of_birth_input:
                    vpd_date_of_birth_input.style('width: 200px;').props('outlined')
                    with ui.menu().props('no-parent-event') as menu2:
                        with ui.date(mask = 'DD/MM/YYYY').bind_value(vpd_date_of_birth_input):
                            with ui.row().classes('justify-end'):
                                ui.button('Close', on_click=menu2.close).props('flat')
                    with vpd_date_of_birth_input.add_slot('append'):
                        ui.icon('edit_calendar').on('click', menu2.open).classes('cursor-pointer')
                        
                vpd_address_input = ui.input(label = 'Address')
                vpd_address_input.style('width: 200px;').props('outlined')
                
                vpd_save_data_button = ui.button(text = 'Save Data', icon = 'person_add', on_click = lambda: vpd.vpd_add_new_data(vpd_full_name_input, vpd_pin_input, vpd_document_number_input, 
                                                                                                                                  vpd_date_of_issue_input, vpd_expiration_date_input, 
                                                                                                                                  vpd_issuing_authority_input, vpd_date_of_birth_input, 
                                                                                                                                  vpd_address_input, vpd_table, vpd_rows_hidden, 
                                                                                                                                  vpd_rows_unhidden, vpd_logs))
                vpd_save_data_button.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
                
                
                
                
            vpd_add_data_button = ui.button(icon = 'person_add', on_click = vpd_dialog.open)
            vpd_add_data_button.tailwind.background_color('transparent')
            vpd_add_data_button.tooltip(text = 'Add new data.')
            
            vpd_remove_data_button = ui.button(icon = 'person_remove', on_click = lambda: globals.global_remove_data_from_tables(vpd_table, 'vpd', vpd_rows_hidden, vpd_rows_unhidden, vpd_logs))
            vpd_remove_data_button.tailwind.background_color('transparent')
            vpd_remove_data_button.tooltip(text = 'Remove data/s selected.')
            
            vpd_data_download_button = ui.button(icon = 'download')
            vpd_data_download_button.tailwind.background_color('transparent')
            vpd_data_download_button.tooltip(text = 'Download data/s selected.')
            
            with ui.dialog() as vpd_dialog1, ui.card():
                vpd_logs = ui.log()
                vpd_logs.style('width: 500px')
                
            vpd_logs_button = ui.button(icon = 'history', on_click = vpd_dialog1.open)
            vpd_logs_button.tailwind.background_color('transparent')
            vpd_logs_button.tooltip(text = 'See your last actions.')
                     
        vpd_columns = [
            {'headerName': 'ID', 'field': 'id', 'filter': 'agTextColumnFilter', 'floatingFilter': True, 'headerCheckboxSelection': True, 'checkboxSelection': True},
            {'headerName': 'Full Name', 'field': 'full_name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'PIN', 'field': 'pin', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Document Number', 'field': 'document_number', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Date of Issue', 'field': 'date_of_issue', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Expiration Date', 'field': 'expiration_date', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Issuing Authority', 'field': 'issuing_authority', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Date of Birth', 'field': 'date_of_birth', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Address', 'field': 'address', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            
        ]
        
        vpd_rows_hidden = []
        vpd_rows_unhidden = []
        
        vpd_table = ui.aggrid(options = {'columnDefs': vpd_columns, 'rowData': vpd_rows_hidden, 
                                          'rowSelection': 'multiple', 'pagination': True,}, theme = "alpine-dark")
        vpd_table.style('height: 545px')
        