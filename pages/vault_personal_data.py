from nicegui import ui
from components import navbar


@ui.page('/vault_personal_data')
def vault_personal_data():
    navbar.navbar()
    with ui.card().style('width: 100%'):
        
        with ui.row().classes('gap-20'):
            vpd_hide_unhide_id_dn_button = ui.button(icon = 'visibility')
            vpd_hide_unhide_id_dn_button.tailwind.background_color('transparent')
            vpd_hide_unhide_id_dn_button.tooltip(text = 'Hide or unhide Identity Number and Document Number of selected data/s.')
            
            vpd_add_data_button = ui.button(icon = 'person_add')
            vpd_add_data_button.tailwind.background_color('transparent')
            vpd_add_data_button.tooltip(text = 'Add new data.')
            
            vpd_remove_data_button = ui.button(icon = 'person_remove')
            vpd_remove_data_button.tailwind.background_color('transparent')
            vpd_remove_data_button.tooltip(text = 'Remove data/s selected.')
            
            vpd_data_download_button = ui.button(icon = 'download')
            vpd_data_download_button.tailwind.background_color('transparent')
            vpd_data_download_button.tooltip(text = 'Download data/s selected.')
            
            vpd_logs_button = ui.button(icon = 'history')
            vpd_logs_button.tailwind.background_color('transparent')
            vpd_logs_button.tooltip(text = 'See your last actions.')
        
        vpd_columns = [
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
        
        vpd_rows_hidden = []
        vpd_rows_unhidden = []
        
        vpd_table = ui.table(
            columns = vpd_columns,
            rows = vpd_rows_hidden,
            selection = 'multiple',
            pagination = 7
        ).style('width: 100%')
        