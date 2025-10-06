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

app.on_startup(lambda : main_page())

app.native.window_args['min_size'] = [1040, 700]
#ui.run(dark= True, title = 'CryptKeep', native =  True, window_size = [1040, 700])
ui.run(dark= True, title = 'CryptKeep')
