from nicegui import ui
from components import navbar
from functions import bc

@ui.page('/breach_checker')
def breach_checker_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%; font-family: Times New Roman'):
        with ui.row():
        
            start_breach_checker_button = ui.button(text = 'Start Breach Checker', on_click = lambda: bc.breach_checker(bc_log, spinner))
            start_breach_checker_button.props('color=white text-color=black').style('text-transform: none; align-self: center; font-size: 20px')
            spinner = ui.spinner()
            spinner.set_visibility(False)
        bc_log = ui.log()