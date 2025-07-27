from nicegui import ui
from components import navbar


@ui.page('/vault_personal_data')
def vault_personal_data():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        
        with ui.row().classes('gap-20'):
            pass
        
        columns = [
            {'name': 'id', 'label': 'ID', 'field': 'id', 'align': 'center'},
            {'name': 'full_name', 'label': 'Full Name', 'field': 'full_name', 'align': 'center'},
            {'name': 'identity_number', 'label': 'Identity Number', 'field': 'identity_number', 'align': 'center'},
            {'name': 'document_number', 'label': 'Document Number', 'field': 'document_number', 'align': 'center'},
            {'name': 'date_of_issue', 'label': 'Date of Issue', 'field': 'date_of_issue', 'align': 'center'},
            {'name': 'expiration_date', 'label': 'Expiration Date', 'field': 'expiration_date', 'align': 'center'},
            {'name': 'issuing_authority', 'label': 'Issuing Authority', 'field': 'issuing_authority', 'align': 'center'},
            {'name': 'date_of_birth', 'label': 'Date of Birth', 'field': 'date_of_birth', 'align': 'center'},
            {'name': 'address', 'label': 'Address', 'field': 'address', 'align': 'center'},
        ]
        
        rows = []
        table_keys = ui.table(
            columns = columns,
            rows = rows,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')