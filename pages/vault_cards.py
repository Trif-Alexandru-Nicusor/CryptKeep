from nicegui import ui
from components import navbar
from functions import vc, globals

@ui.page('/vault_cards')
def vault_cards_page():
    
    from datetime import datetime
    
    navbar.navbar()
    
    with ui.card().style('width: 100%').style('font-family: Times New Roman'):
        
        ui.label('Vault Cards').style('font-size: 25px; align-self: center')
        
        with ui.row().style('align-self: center'):
            vc_hide_unhide_button = ui.button(icon = 'visibility', on_click = lambda: globals.global_hide_unhide_things(vc_hide_unhide_button, globals.vc_rows_hidden, globals.vc_rows_unhidden, vc_table, vc_logs, 'vc'))
            vc_hide_unhide_button.props('color=transparent')
            vc_hide_unhide_button.tooltip(text = 'Hide or unhide the card/s number and CVV.')
            
            with ui.dialog() as dialog, ui.card().classes('scrollbar-custom').style('font-family: Times New Roman'):
                vc_type_select = ui.select(label = 'Type', options = ['Credit', 'Debit'])
                vc_type_select.style('width: 225px; align-self: center').props('outlined')
                
                vc_bank_input = ui.input(label = 'Bank')
                vc_bank_input.style('width: 225px; align-self: center').props('outlined')
                
                vc_cardholders_name = ui.input(label = 'Cardholder’s Name')
                vc_cardholders_name.style('width: 225px; align-self: center').props('outlined')
                
                vc_card_number_input = ui.input(label = 'Cardholder’s Name')
                vc_card_number_input.style('width: 225px; align-self: center').props('outlined')
                
                with ui.expansion(text='Expiration date', icon='calendar_month').style('border: 1px solid #ccc; border-radius: 8px; width: 225px;'):
                    
                    vc_expiration_date_month_select = ui.select(label = 'Month', options = [str(i) for i in range(1, 13)], with_input = True)
                    vc_expiration_date_month_select.style('width: 190px; align-self: center').props('outlined')
                
                    vc_expiration_date_year_select = ui.select(label = 'Year', options = [str(year) for year in range(datetime.now().year, datetime.now().year + 31)], with_input = True)
                    vc_expiration_date_year_select.style('width: 190px; align-self: center').props('outlined')

                vc_cvv_input = ui.input(label = 'CVV')
                vc_cvv_input.style('width: 225px; align-self: center').props('outlined')
                
                vc_save_card = ui.button(text = 'Save Card', icon = 'add_card', on_click = lambda: vc.vc_add_new_card(vc_type_select, vc_bank_input, vc_cardholders_name, vc_card_number_input,
                                                                                                                      vc_expiration_date_month_select, vc_expiration_date_year_select, vc_cvv_input,
                                                                                                                      vc_table, globals.vc_rows_hidden, globals.vc_rows_unhidden, vc_logs))
                vc_save_card.props('flat color=white text-color=white').style('text-transform: none; align-self: center')
                             
            vc_add_card_s_button = ui.button(icon = 'add_card', on_click = dialog.open)
            vc_add_card_s_button.props('color=transparent')
            vc_add_card_s_button.tooltip(text = 'Add a new card.')
            
            vc_remove_card_s_button = ui.button(icon = 'credit_card_off', on_click = lambda: globals.global_remove_data_from_tables(vc_table, 'vc', globals.vc_rows_hidden, globals.vc_rows_unhidden, vc_logs))
            vc_remove_card_s_button.props('color=transparent')
            vc_remove_card_s_button.tooltip(text = 'Remove the card/s selected')
            
            vc_download_card_s_info = ui.button(icon = 'download')
            vc_download_card_s_info.props('color=transparent')
            vc_download_card_s_info.tooltip(text = 'Download card/s selected.')
                        
            with ui.dialog() as dialog1, ui.card().style('font-family: Times New Roman'):
                vc_logs = ui.log()
                vc_logs.style('width: 500px')
                
            vc_logs_button = ui.button(icon = 'history', on_click = dialog1.open)
            vc_logs_button.props('color=transparent')
            vc_logs_button.tooltip(text = 'See your last actions.')
            
        vc_columns = [
            {'headerName': 'ID', 'field': 'id', 'filter': 'agTextColumnFilter', 'floatingFilter': True, 'headerCheckboxSelection': True, 'checkboxSelection': True},
            {'headerName': 'Type', 'field': 'type', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Bank', 'field': 'bank', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Cardholder’s Name', 'field': 'cardholders_name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Card Number', 'field': 'card_number', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'CVV', 'field': 'cvv', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
            {'headerName': 'Expiration Date', 'field': 'expiration_date', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
        ]
        

        
        with ui.scroll_area().style('height: 435px;'):
            vc_table = ui.aggrid(options = {'columnDefs': vc_columns, 'rowData': globals.vc_rows_hidden, 'rowSelection': 'multiple', 'pagination': True,
                                             'enableCellTextSelection': True, 'clipboard': True,
                                             'paginationPageSize': 6, 'paginationPageSizeSelector': [6, 10, 15, 20, 25, 30, 35, 40, 45, 50]}, theme = "alpine")
            vc_table.style('min-width: 1400px; align-self:center; height: 400px;')
            vc_table.props('data-ag-theme-mode=dark')