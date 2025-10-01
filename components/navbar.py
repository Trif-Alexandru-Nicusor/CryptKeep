from nicegui import ui, app

def navbar():
    ui.add_css('''
               .q-tooltip {
                    font-size: 15px;
                }
                .q-drawer__content::-webkit-scrollbar {
                    display: none;
                }

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
                .scrollbar-custom::-webkit-scrollbar {
                    width: 0px;
                }
                .scrollbar-custom::-webkit-scrollbar-track {
                    background: transparent;
                }
                .scrollbar-custom::-webkit-scrollbar-thumb {
                    background-color: transparent;
                    border-radius: 10px;
                }
                .q-field input {
                    font-size: 18px;
                }
                .ag-theme-alpine-dark .ag-cell {
                    font-size: 14px !important;
                    font-family: 'Times New Roman' !important;
                    text-align: center !important;
                    align-items: center;
                    justify-content: center;
                }
                .ag-theme-alpine-dark .ag-header-cell-label {
                    font-size: 16px;
                    justify-content: center !important;
                    font-family: 'Times New Roman' !important;
                }
            ''')
    
    with ui.left_drawer(bordered = True, elevated = True).props('width=246').style('font-family: Times New Roman') as side_bar:
        
        with ui.menu_item(on_click = lambda: ui.navigate.to('/main')).style('width: 100%'):
            ui.label(text = 'CryptKeep').style('font-size: 26px')
            
        with ui.expansion(text = 'Vault', icon = 'enhanced_encryption').style('width: 100%; font-size: 25px'):
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/vault_accounts')).style('width: 100%'):
                ui.icon(name = 'account_circle', size = '25px')
                ui.label(text = 'Accounts').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/vault_keys')).style('width: 100%'):
                ui.icon(name = 'key', size = '25px')
                ui.label(text = 'Keys').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/vault_cards')).style('width: 100%'):
                ui.icon(name = 'credit_card', size = '25px')
                ui.label(text = 'Cards').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/vault_personal_data')).style('width: 100%'):
                ui.icon(name = 'person', size = '25px')
                ui.label(text = 'PersonaI Data').style('font-size: 20px; position: relative; right: -10px')
                
        with ui.expansion(text = 'Tools', icon = 'handyman').style('width: 100%; font-size: 25px'):
            
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/password_generator')).style('width: 100%'):
                ui.icon(name = 'password', size = '25px')
                ui.label(text = 'Password Generator').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/breach_checker')).style('width: 100%'):
                ui.icon(name = 'security', size = '25px')
                ui.label(text = 'Breach Checker').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/')).style('width: 100%'):
                ui.icon(name = 'history', size = '25px')
                ui.label(text = 'Activity Log').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/')).style('width: 100%'):
                ui.icon(name = 'find_in_page', size = '25px')
                ui.label(text = 'Duplicate Finder').style('font-size: 20px; position: relative; right: -10px')
                
            with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/')).style('width: 100%'):
                ui.icon(name = 'insights', size = '25px')
                ui.label(text = 'Usage Stats').style('font-size: 20px; position: relative; right: -10px')

        with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/')).style('width: 100%'):
            ui.icon(name = 'settings', size = '25px')
            ui.label(text = 'Settings').style('font-size: 25px; position: relative; right: -25px; top: -5px')
            
        ui.separator()
        
        with ui.menu_item(on_click = lambda: ui.navigate.to(target = '/')).style('width: 100%'):
            ui.icon(name = 'logout', size = '25px')
            ui.label(text = 'Log out').style('font-size: 25px; position: relative; right: -25px; top: -5px')
    
    ui.button(icon='menu', on_click=side_bar.toggle).style('position:relative; z-index: 1000').tailwind.background_color('transparent')
