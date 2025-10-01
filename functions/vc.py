from nicegui import ui
from functions.crud import add_in_vault_cards
def vc_add_new_card(type, bank, cardholders_name, card_number, expiration_date_month, expiration_date_year, cvv, table, rows_hidden, rows_unhidden, logs):
    
    
    if not type.value or not bank.value or not cardholders_name.value or not card_number.value or not expiration_date_month.value or not expiration_date_year.value or not cvv.value:
        
        logs.push('Failed to add new data because\nyou didnt filled all the fields.', classes = 'text-red')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        ui.notify(message='You need to complete all fields.', position = 'bottom', type = 'negative')
        
    else:
        
        expiration_date = expiration_date_month.value + '/' + expiration_date_year.value
        
        new_id  = (max([r['id'] for r in rows_hidden], default=0) + 1) if rows_hidden else 1

        rows_hidden.append({'id': new_id, 'type': type.value, 'bank': bank.value, 'cardholders_name': cardholders_name.value, 'card_number': '*' * len(card_number.value), 'expiration_date': expiration_date, 'cvv': '*' * len(cvv.value)})
        rows_unhidden.append({'id': new_id, 'type': type.value, 'bank': bank.value, 'cardholders_name': cardholders_name.value, 'card_number': card_number.value, 'expiration_date': expiration_date, 'cvv': cvv.value})
        
        logs.push(line = f'New card added for[\ntype:{type.value}\nbank: {bank.value}\ncardholder`s name: {cardholders_name.value}]', classes = 'text-green')
        logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
        
        add_in_vault_cards(new_id, type.value, bank.value, cardholders_name.value, card_number.value, cvv.value, expiration_date)
        
        type.set_value(None)
        bank.set_value(None)
        cardholders_name.set_value(None)
        card_number.set_value(None)
        expiration_date_month.set_value(None)
        expiration_date_year.set_value(None)
        cvv.set_value(None)
        
        table.options['rowData'] = rows_hidden
        table.update()
        
        ui.notify(message = 'New card added.', position = 'bottom', type = 'positive')