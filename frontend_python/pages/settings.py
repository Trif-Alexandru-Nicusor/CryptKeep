from nicegui import ui
from components import navbar

@ui.page('/settings')
def settings_page():
    navbar.navbar()
    
    with ui.card():
        with ui.expansion(text = 'Storage Settings'):
            with ui.column():
                ui.checkbox(text = 'Save and load from local storage')
                ui.checkbox(text = 'Save and load from cloud storage')