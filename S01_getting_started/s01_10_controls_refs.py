import flet as ft

def main(page):
    page.window_width = 700
    page.window_height = 400 
    
    txt_first_name = ft.Ref[ft.TextField]() #ft.TextField(label="First Name", autofocus=True, hint_text="Please enter your first name")
    txt_last_name = ft.Ref[ft.TextField]() #ft.TextField(label="Last Name", hint_text="Please enter your last name")
    col_controles =ft.Ref [ft.Column]()
    
    def saludar_clicked(e):
        col_controles.current.controls.append(ft.Text(f'Hola {txt_first_name.current.value} {txt_last_name.current.value}'))
        txt_first_name.current.value = ""
        txt_last_name.current.value = ""        
        page.update()
        txt_first_name.current.focus()
    
    
    page.add(
        ft.TextField(ref=txt_first_name, label="First Name", autofocus=True, hint_text="Please enter your first name"),
        ft.TextField(ref=txt_last_name,label="Last Name", hint_text="Please enter your last name"),
        ft.ElevatedButton("Saludar", on_click=saludar_clicked),
        ft.Column(ref=col_controles),
    )

ft.app(target=main)