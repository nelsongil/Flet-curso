import flet as ft

def main(page: ft.Page):
    page.window_width = 700
    page.window_height = 400 
    
    def agregar_tarea_clicked(event):
        if txt_nueva_tarea.value != "":
            page.add(ft.Checkbox(label=txt_nueva_tarea.value))
            txt_nueva_tarea.value = ""
            page.update()
    
    txt_nueva_tarea = ft.TextField(hint_text='¿Cuál tarea desea agregar?',width=300)
    
    btn_agregar_tarea = ft.ElevatedButton('Agregar', on_click=agregar_tarea_clicked)
    
    page.add(ft.Row([txt_nueva_tarea, btn_agregar_tarea]))

ft.app(target=main)