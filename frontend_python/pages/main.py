from nicegui import ui
from components import navbar

@ui.page('/main')
def main_page():
    navbar.navbar()
    with ui.card().style('width: 100%; background-color: rgba(255, 255, 255, 0.1);'):
        ui.label(text = 'CryptKeep').style('font-size: 50px; align-self: center')
        ui.label(text = 'By: Trif Alexandru-Nicusor').style('font-size: 45px; align-self: center')
        with ui.row().style('align-self: center; position: relative; right: 30px'):
            ui.image(source = 'images/discord.png').style('width: 100px; position: relative; bottom: 15px; left: 30px')
            ui.label(text = 'manafique.alex').style('font-size: 30px; user-select: text; -webkit-user-select: text; cursor: text')
        ui.image(source = 'images/linkedin.png').on(type = 'click', handler = lambda: ui.navigate.to('https://www.linkedin.com/in/alexandru-nicusor-trif-146a35250')).classes(add = 'cursor-pointer').style('width: 200px; align-self: center')
        ui.image(source = 'images/github.png').on(type = 'click', handler = lambda: ui.navigate.to('https://github.com/Trif-Alexandru-Nicusor')).classes(add = 'cursor-pointer').style('width: 200px; align-self: center')
