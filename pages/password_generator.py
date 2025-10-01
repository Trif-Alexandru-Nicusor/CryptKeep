from nicegui import ui
from components import navbar

@ui.page('/password_generator')
def password_generator_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%; font-family: Times New Roman'):
        with ui.column().style('align-self: center'):
            with ui.row():
                ui.checkbox('a-z')
                ui.checkbox('A-Z')
                ui.checkbox('0-9')
                ui.checkbox('!-*')
            with ui.row():
                ui.number(label = 'Max Characters').props('outlined').style('max-width: 125px')
                ui.button(text = 'Generate Password').tailwind.background_color('white').text_color('black').text_transform('normal-case')
            ui.input(label = 'Generated Password').props('outlined').style('max-width: 160px; align-self:center')