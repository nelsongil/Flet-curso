import flet as ft

def main(page: ft.Page):
    page.window_width = 700
    page.window_height = 400 
    
    txt_first_name = ft.TextField(label="First Name", hint_text="Please enter your first name")
    txt_last_name = ft.TextField(label="Last Name", hint_text="Please enter your last name")
    
    # Propiedad Disable individualizada:
    #txt_first_name.disabled = True
    
    col_controles = ft.Column(controls=[txt_first_name,txt_last_name])
    
    # Propiedad Disable en la columna:
    #col_controles.disabled=True
    
    page.add(col_controles)

ft.app(target=main)