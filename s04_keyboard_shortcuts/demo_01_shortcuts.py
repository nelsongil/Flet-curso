import flet as ft

def main(page:ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f'Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}'
            )
        )
        
    page.on_keyboard_event = on_keyboard
    
    page.add(ft.Text('Presione cualquier tecla con una combinación (Control, Alt, Shift, Commmand)...'))
    

ft.app(target=main)