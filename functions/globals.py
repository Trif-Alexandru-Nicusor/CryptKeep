from nicegui import ui
import json
from functions.crud import delete_records_global

async def global_remove_data_from_tables(table, which_table, rows_hidden, rows_unhidden, logs):

    selected_rows = await table.get_selected_rows()
    
    if selected_rows != []:
        
        filtered_rows = [
            {k: v for k, v in row.items() if '*' not in str(v)}
            for row in rows_hidden
        ]
        
        if which_table == 'va':
            
            for row in selected_rows:
                id = row.get("id")
                if id:
                    delete_records_global(id, 'vault_accounts')
                    
            logs.push(f"Account/s removed.\n{json.dumps(filtered_rows, indent=1)}", classes='text-green')
            logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
            ui.notify(message='Account/s removed.', position='bottom', type='positive')
        
        elif which_table == 'vk':
            
            logs.push(f'Key/s removed.\n{json.dumps(filtered_rows, indent=1)}', classes = 'text-green')
            logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
            ui.notify(message='Key/s removed.', position='bottom', type='positive')
        
        elif which_table == 'vc':
            
            logs.push(f'Card/s removed.\n{json.dumps(filtered_rows, indent=1)}', classes = 'text-green')
            logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
            ui.notify(message='Card/s removed.', position='bottom', type='positive')
        
        elif which_table == 'vpd':
            
            logs.push(f'Data removed.\n{json.dumps(filtered_rows, indent=1)}', classes = 'text-green')
            logs.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', classes = 'text-grey')
            ui.notify(message='Data removed', position='bottom', type='positive')
    
        ids_to_delete = [row['id'] for row in selected_rows]
        
        rows_hidden[:] = [row for row in rows_hidden if row['id'] not in ids_to_delete]
        rows_unhidden[:] = [row for row in rows_unhidden if row['id'] not in ids_to_delete]
        
        table.options['rowData'] = rows_hidden
        table.update()
        
    else:
        
        logs.push('You need to select at least 1 row', classes = 'text-red')
        return ui.notify(message='You need to select at least 1 row.', position='bottom', type='negative')
    
hide_unhide_things = False
async def global_hide_unhide_things(hide_unhide, rows_hidden, rows_unhidden, table, logs,what_to_hide_unhide):
    
    global hide_unhide_things
    
    what_to_hide_unhide_dict = {
        'va': ['Passwords unhidden.', 'Passwords hidden.'],
        'vc': ['Card number & VCC unhidden.', 'Card number & VCC hidden.'],
        'vk': ['Key/s unhidden.', 'Key/s uidden.'],
        'vpd': ['PIN/s and Document/s Number unhidden.', 'PIN/s and Document/s Number hidden.']
    }
    

    selected_rows = await table.get_selected_rows()

    if hide_unhide.icon == 'visibility':
        
        hide_unhide.set_icon('visibility_off')
        
        for wathd in what_to_hide_unhide_dict:
            
            if what_to_hide_unhide == wathd:
                
                logs.push(line = what_to_hide_unhide_dict[what_to_hide_unhide][0], classes='text-grey')
                ui.notify(message = what_to_hide_unhide_dict[what_to_hide_unhide][0], position='bottom', type='positive')
            
        new_data = []
        
        for row in table.options['rowData']:
            
            match = next((unhidden for unhidden in rows_unhidden if unhidden['id'] == row['id']), None)
            
            if row in selected_rows and match:
                
                new_data.append(match)
                
            else:
                
                new_data.append(row)
                
        table.options['rowData'] = new_data
        table.update()
        hide_unhide_things = True

    else:
        
        hide_unhide.set_icon('visibility')
        
        for wathd in what_to_hide_unhide_dict:
            
            if what_to_hide_unhide == wathd:
                
                logs.push(line = what_to_hide_unhide_dict[what_to_hide_unhide][1], classes='text-grey')
                ui.notify(message = what_to_hide_unhide_dict[what_to_hide_unhide][1], position='bottom', type='positive')
                
        new_data = []
        
        for row in table.options['rowData']:
            
            match = next((hidden for hidden in rows_hidden if hidden['id'] == row['id']), None)
            
            if row in selected_rows and match:
                
                new_data.append(match)
                
            else:
                
                new_data.append(row)
                
        table.options['rowData'] = new_data
        table.update()
        hide_unhide_things = False