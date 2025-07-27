from nicegui import ui
from components import navbar

@ui.page('/vault_cards')
def vault_cards_page():
    from datetime import datetime
    navbar.navbar()
    
    with ui.card().style('width: 100%'):
        with ui.row().classes('gap-24'):
            vc_hide_unhide_button = ui.button(icon = 'visibility')
            vc_hide_unhide_button.tailwind.background_color('transparent')
            vc_hide_unhide_button.tooltip(text = 'Hide or unhide the card/s number and CVV.')
            
            with ui.dialog() as dialog, ui.card():
                vc_type_select = ui.select(label = 'Type', options = ['Credit', 'Debit'])
                vc_type_select.style('width: 225px; align-self: center').props('outlined')
                
                vc_name_on_card_input = ui.input(label = 'Name On Card')
                vc_name_on_card_input.style('width: 225px; align-self: center').props('outlined')
                
                vc_card_number_input = ui.input(label = 'Name on Card')
                vc_card_number_input.style('width: 225px; align-self: center').props('outlined')
                with ui.expansion(text='Expiration date', icon='calendar_month').style('border: 1px solid #ccc; border-radius: 8px; width: 225px'):
                    vc_expiration_date_month_select = ui.select(label = 'Month', options = [str(i) for i in range(1, 13)])
                    vc_expiration_date_month_select.style('width: 200px; align-self: center').props('outlined')
                
                    vc_expiration_date_day_select = ui.select(label = 'Year', options = [str(year) for year in range(datetime.now().year, datetime.now().year + 31)])
                    vc_expiration_date_day_select.style('width: 200px; align-self: center').props('outlined')
                
                vc_cvv_input = ui.input(label = 'CVV')
                vc_cvv_input.style('width: 225px; align-self: center').props('outlined')
                
                vc_save_card = ui.button(text = 'Save Card', icon = 'add_card')
                vc_save_card.tailwind.background_color('white').text_transform('normal-case').align_self('center').text_color('black')
                             
            vc_add_card_s_button = ui.button(icon = 'add_card', on_click = dialog.open)
            vc_add_card_s_button.tailwind.background_color('transparent')
            vc_add_card_s_button.tooltip(text = 'Add a new card.')
            
            vc_remove_card_s_button = ui.button(icon = 'credit_card_off')
            vc_remove_card_s_button.tailwind.background_color('transparent')
            vc_remove_card_s_button.tooltip(text = 'Remove the card/s selected')
            
            vc_download_card__s_info = ui.button(icon = 'download')
            vc_download_card__s_info.tailwind.background_color('transparent')
            vc_download_card__s_info.tooltip(text = 'Download card/s selected.')
                        
            with ui.dialog() as dialog1, ui.card():
                vc_logs = ui.log()
                vc_logs.style('width: 500px')
                
            vc_logs_button = ui.button(icon = 'history', on_click = dialog1.open)
            vc_logs_button.tailwind.background_color('transparent')
            vc_logs_button.tooltip(text = 'See your last actions.')
            
        vc_columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'type', 'label': 'Type', 'field': 'type', 'align': 'center'},
            {'name': 'name_on_card', 'label': 'Name on Card', 'field': 'cardholders_name', 'align': 'center'},
            {'name': 'card_number', 'label': 'Card Number', 'field': 'card_number', 'align': 'center'},
            {'name': 'expiration_date', 'label': 'Expiration Date', 'field': 'expiration_date', 'align': 'center'},
            {'name': 'cvv', 'label': 'CVV', 'field': 'cvv', 'align': 'center'},
        ]
        vc_rows_hidden = []
        vc_rows_unhidden = []
        vc_table = ui.table(
            columns = vc_columns,
            rows = vc_rows_hidden,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')