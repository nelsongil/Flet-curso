from math import pi
import flet as ft 

def main(page: ft.Page):
    
    contenedor = ft.Container(
        width=100,
        height=70,
        bgcolor="blue",
        border_radius=5,
        rotate=ft.transform.Rotate(0,alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(duration=300, curve=ft.AnimationCurve.BOUNCE_OUT),
    )
    
    def animate(e):
        contenedor.rotate.angle += pi / 2
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        contenedor,
        ft.ElevatedButton("Animate!", on_click=animate),
    )
    
    
ft.app(target=main)