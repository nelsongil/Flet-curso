import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Ruta inicial: {page.route}"))
    
    def route_change(route):
        page.add(ft.Text(f"Nueva ruta: {route.route}"))
        
    page.on_route_change = route_change
    page.update()
    

ft.app(target=main, view=ft.AppView.WEB_BROWSER)