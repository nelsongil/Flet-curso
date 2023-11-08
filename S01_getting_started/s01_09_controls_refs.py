import flet as ft

def main(page):
    page.window_width = 700
    page.window_height = 400 
    
    txt_first_name = ft.TextField(label="First Name", autofocus=True, hint_text="Please enter your first name")
    txt_last_name = ft.TextField(label="Last Name", hint_text="Please enter your last name")
    col_controles = ft.Column()
    
    def saludar_clicked(e):
        col_controles.controls.append(ft.Text(f'Hola {txt_first_name.value} {txt_last_name.value}'))
        txt_first_name.value = ""
        txt_last_name.value = ""        
        page.update()
        txt_first_name.focus()
    
    btn_saludar = ft.ElevatedButton('Saludar', on_click=saludar_clicked)
    

    
    page.add(
        txt_first_name,
        txt_last_name,
        btn_saludar,
        col_controles
    )

ft.app(target=main)