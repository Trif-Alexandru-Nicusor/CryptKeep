from components.navbar import *
from pages.main import *
from pages.vault_accounts import *
from pages.vault_keys import *
from pages.vault_cards import *
from pages.vault_personal_data import *
from nicegui import ui, app



main_page()

app.native.window_args['min_size'] = [1040, 700]
ui.run(dark= True, title = 'CryptKeep', native =  True, window_size = [1040, 700])