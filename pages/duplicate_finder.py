from nicegui import ui
from components import navbar
from functions.crud import find_duplicate_passwords

@ui.page('/duplicate_finder')
def duplicate_finder_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%').style('font-family: Times New Roman'):
        
        find_duplicates_button = ui.button(text = 'Find duplicates', on_click = lambda: find_duplicate_passwords(df_logs))
        find_duplicates_button.props('color=white text-color=black').style('text-transform: none; font-size: 20px')
        
        df_logs = ui.log()