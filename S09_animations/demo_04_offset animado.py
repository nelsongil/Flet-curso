import flet as ft

def main(page: ft.Page):

    contenedor = ft.Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        offset=ft.transform.Offset(-2, 2),
        animate_offset=ft.animation.Animation(1000),
    )

    def animate(e):
        contenedor.offset = ft.transform.Offset(0, 0)
        contenedor.update()

    page.add(
        contenedor,
        ft.ElevatedButton("Reveal!", on_click=animate),
    )

ft.app(target=main)