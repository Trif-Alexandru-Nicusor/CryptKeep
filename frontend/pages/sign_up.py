from nicegui import ui

@ui.page('/sign_up')
def sign_up_page():
    ui.add_css('''
                .q-field.q-field--outlined {
                    --q-primary: white;
                    --q-field-border-color: white;
                    --q-field-label-color: white;
                    transition: border-color 0.3s ease, color 0.3s ease;
                }
                .q-field.q-field--outlined.q-field--focused {
                    --q-primary: white;
                    --q-field-border-color: white;
                    --q-field-label-color: white;
                }
                .q-field.q-field--outlined.q-field--highlighted {
                    --q-primary: white;
                    --q-field-border-color: white;
                    --q-field-label-color: white;
                }
                :root {
                    --q-primary: white !important;
                }
                .q-field input {
                    font-size: 20px;
                }
            ''')

    with ui.card().style('align-self: center; align-items: center; font-family: "Times New Roman";').classes('gap-y-7'):
        ui.label('Sign Up').style('font-size: 30px; font-weight: bold')
        
        first_name_input = ui.input(label = 'First Name')
        first_name_input.props('outlined').style('width: 300px;')
        
        last_name_input = ui.input(label = 'Last Name')
        last_name_input.props('outlined').style('width: 300px')
        
        username_input = ui.input(label = 'Username')
        username_input.props('outlined').style('width: 300px')
        
        email_input = ui.input(label = 'Email')
        email_input.props('outlined').style('width: 300px')
        
        password_input = ui.input(label = 'Password', password = True, password_toggle_button = True)
        password_input.props('outlined').style('width: 300px')
        
        sign_up_button = ui.button(text = 'Sign Up')
        sign_up_button.tailwind.background_color('white').text_color('black').text_transform('normal-case').align_self('center').font_size('lg')
        
        ui.link(text = 'Already have an account? Login In', target = '/login').tailwind.text_color('white').font_size('lg')