from nicegui import ui

@ui.page('/login')
def login_page():
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

    with ui.card().style('align-self: center; align-items: center; font-family: "Times New Roman"; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)').classes('gap-y-10'):
        ui.label('Log In').style('font-size: 30px; font-weight: bold')
        
        username_input = ui.input(label = 'Username')
        username_input.props('outlined').style('width: 300px;')
        
        password_input = ui.input(label = 'Password', password = True, password_toggle_button = True)
        password_input.props('outlined').style('width: 300px')
        
        with ui.row():
            
            local_cloud_storage_radio = ui.radio(options = ['Local', 'Cloud'])
            local_cloud_storage_radio.props('inline color=white').style('font-size: 20px')
            
        log_in_button = ui.button(text = 'Log In')
        log_in_button.tailwind.background_color('white').text_color('black').text_transform('normal-case').align_self('center').font_size('lg')
        
        ui.link(text = "Don't have an account? Sign Up", target = '/sign_up').tailwind.text_color('white').font_size('lg')