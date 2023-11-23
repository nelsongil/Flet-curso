import flet as ft


def main(page: ft.Page):
    page.title = "Containers with background color"

    c1 = ft.Container(
        content=ft.ElevatedButton("Elevated Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton(
            "Elevated Button with opacity=0.5 in Container", opacity=0.5
        ),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c3 = ft.Container(
        content=ft.OutlinedButton("Outlined Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )
    page.add(c1, c2, c3)


ft.app(target=main)