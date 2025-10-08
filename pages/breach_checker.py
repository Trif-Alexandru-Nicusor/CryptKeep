from nicegui import ui
from components import navbar
from functions import bc
import asyncio

@ui.page('/breach_checker')
def breach_checker_page():
    navbar.navbar()

    with ui.card().style('width: 100%; font-family: Times New Roman'):
        with ui.row():
            start_breach_checker_button = ui.button(
                text='Start Breach Checker',
                on_click=lambda: asyncio.create_task(bc.breach_checker_async(bc_log, spinner))
            )
            start_breach_checker_button.props('color=white text-color=black').style('text-transform: none; align-self: center; font-size: 20px')
            spinner = ui.spinner(size = '50px', color = 'white', type='ios')
            spinner.set_visibility(False)
        bc_log = ui.log()
