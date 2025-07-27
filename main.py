from components.navbar import *
from pages.main import *
from pages.vault_accounts import *
from pages.vault_keys import *
from pages.vault_cards import *
from pages.vault_personal_data import *
from nicegui import ui

main_page()
ui.run(dark= True, title = 'CryptKeep')