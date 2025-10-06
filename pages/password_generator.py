from nicegui import ui
from components import navbar
from functions import pg

@ui.page('/password_generator')
def password_generator_page():
    
    navbar.navbar()
    
    with ui.card().style('width: 100%; font-family: Times New Roman'):
        
        ui.label('Password Generator').style('font-size: 25px; align-self: center')
        
        with ui.column().style('align-self: center'):
            
            with ui.row():
                
                lower_input = ui.checkbox('a-z')
                lower_input.style('font-size: 20px')
                
                upper_input = ui.checkbox('A-Z')
                upper_input.style('font-size: 20px')

                digits_input = ui.checkbox('0-9')
                digits_input.style('font-size: 20px')
                
                symbols_input = ui.checkbox('!-*')
                symbols_input.style('font-size: 20px')
                
            with ui.row():
                
                max_character_input = ui.number(label = 'Max Characters')
                max_character_input.props('outlined').style('max-width: 125px; font-size: 20px')
                
                generate_button = ui.button(text = 'Generate Password', on_click = lambda: pg.generate_password(int(max_character_input.value), lower_input.value, upper_input.value, digits_input.value, symbols_input.value, generated_password_input))
                generate_button.style('font-size: 18px')
                generate_button.props('color=white text-color=black').style('text-transform: none; align-self: center')
                
            generated_password_input = ui.input(label = 'Generated Password')
            generated_password_input.props('outlined').style('max-width: 160px; align-self:center')