from nicegui import ui
from components import navbar

@ui.page('/breach_checker')
def breach_checker_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%; font-family: Times New Roman'):
        ui.button(text = 'Start Breach Checker').tailwind.background_color('white').text_color('black').text_transform('normal-case')
        ui.log()