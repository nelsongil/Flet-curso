import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page:ft.Page):
    row = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(row)
    
    for i in range(5000):
        row.controls.append(
            ft.Container(
                ft.Text(f'Item {i}'),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_400,
                border_radius=ft.border_radius.all(5)
            )
        )
    page.update()
    

ft.app(target=main)