from components.navbar import *
from pages.main import *
from pages.vault_accounts import *
from pages.vault_keys import *
from pages.vault_cards import *
from pages.vault_personal_data import *
from nicegui import ui, app
from pages.settings import *
from pages.password_generator import *
from pages.breach_checker import *
from functions.crud import get_vault_values
import functions.globals
app.on_startup(lambda : startup())

def startup():
    
    main_page()
    
    globals.va_rows_hidden, globals.va_rows_unhidden = get_vault_values(
        table_name='vault_accounts',
        columns=['id','type','name','email_id_username','password'],
        mask_columns=['password']
    )

    globals.vc_rows_hidden, globals.vc_rows_unhidden = get_vault_values(
        table_name='vault_cards',
        columns=['id','type','bank','cardholders_name','card_number','cvv','expiration_date'],
        mask_columns=['card_number','cvv']
    )

    globals.vk_rows_hidden, globals.vk_rows_unhidden = get_vault_values(
        table_name='vault_keys',
        columns=['id','name','key'],
        mask_columns=['key']
    )
    
    globals.vpd_rows_hidden, globals.vpd_rows_unhidden = get_vault_values(
        table_name='vault_personal_data',
        columns=['id', 'full_name', 'pin', 'document_number', 'date_of_issue', 'expiration_date', 'issuing_authority', 'date_of_birth', 'address'],
        mask_columns=['pin', 'document_number'])
    
app.native.window_args['min_size'] = [1040, 700]
ui.run(dark= True, title = 'CryptKeep', native =  True, window_size = [1040, 700])
#ui.run(dark= True, title = 'CryptKeep')
