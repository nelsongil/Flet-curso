import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("Python"),
            ft.Text("Flet"),
            ft.Text("Row")
        ])
    )

ft.app(target=main)