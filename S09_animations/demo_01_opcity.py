import flet as ft 

def main(page: ft.Page):
    contenedor = ft.Container(
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.Alignment(0.1, 1),
            colors=[
                "0xff1f005c",
                "0xff5b0060",
                "0xff870160",
                "0xffac255e",
                "0xffca485c",
                "0xffe16b5c",
                "0xfff39060",
                "0xffffb56b",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
        ),
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        animate_opacity=300,
    )
    
    def animate_opacity(e):
        contenedor.opacity = 0 if contenedor.opacity == 1 else 1
        contenedor.update()
        
    page.add(
        contenedor,ft.ElevatedButton(
            "Animar opacidad",
            on_click=animate_opacity,
            ),
    )
    
ft.app(target=main)