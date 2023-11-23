import flet as ft 

def main(page:ft.Page):
    page.title = "Screen Reader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def on_keyboard(e: ft.KeyboardEvent):
        print(e)
        if e.key == "Z" and e.ctrl and e.alt:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()
            
    page.on_keyboard_event = on_keyboard
    
    txt_number = ft.Text("0", size=40)
    
    def button_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
        
    page.add(
        txt_number,
        ft.Text("Presione CTRL+S para cambiar depurador semántico"),
        ft.FloatingActionButton(icon=ft.icons.ADD, tooltip="Incrementar número", on_click=button_click),
    )
    
ft.app(target=main)