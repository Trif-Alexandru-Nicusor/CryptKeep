from nicegui import ui
from components import navbar

@ui.page('/vault_cards')
def vault_cards_page():
    navbar.navbar()
    
    with ui.card().style('width: 100%'):
        with ui.row().classes('gap-24'):
            hide_unhide_credit_cards_button = ui.button(icon = 'visibility')
            
            with ui.dialog() as dialog, ui.card():
                type_card_select = ui.select(label = 'Type', options = ['Credit', 'Debit'])
                name_on_card_input = ui.input(label = 'Name On Card')
                card_number_input = ui.input(label = 'Name on Card')
                ui.label('Expiration Date')
                expiration_date_month_input = ui.select(label = 'Month', options = [str(i) for i in range(1, 32)])
                expiration_date_day_input = ui.select(label = 'Year', options = [])
                cvv_input = ui.input(label = 'CVV')
                
            add_card_button = ui.button(icon = 'add_card', on_click = dialog.open)
            
            remove_card_button = ui.button(icon = 'credit_card_off')
            
            download_card_info = ui.button(icon = 'download')
            
            with ui.dialog() as dialog1, ui.card():
                logs = ui.log()
                logs.style('width: 500px')
                
            logs_vault_cards_button = ui.button(icon = 'history', on_click = dialog1.open)
            
        columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'type', 'label': 'Type', 'field': 'type', 'align': 'center'},
            {'name': 'name_on_card', 'label': 'Name on Card', 'field': 'cardholders_name', 'align': 'center'},
            {'name': 'card_number', 'label': 'Card Number', 'field': 'card_number', 'align': 'center'},
            {'name': 'expiration_date', 'label': 'Expiration Date', 'field': 'expiration_date', 'align': 'center'},
            {'name': 'cvv', 'label': 'CVV', 'field': 'cvv', 'align': 'center'},
        ]
        rows = []
        table_credit_cards = ui.table(
            columns = columns,
            rows = rows,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')