import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de rutas"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visita la Tienda", on_click=lambda _: page.go("/tienda")),
                ],
            )
        )
        if page.route == "/tienda":
            page.views.append(
                ft.View(
                    "/tienda",
                    [
                        ft.AppBar(title=ft.Text("Tienda"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Volver al inicio", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)