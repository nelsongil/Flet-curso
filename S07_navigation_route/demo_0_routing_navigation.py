import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de rutas"
    
    print ('Ruta inicial', page.route)
    
    def route_change(e):
        print('ua cambiada:', e.route)
        page.views.clear()
        
        page.views.append(
            ft.View(
                '/',
                [
                    ft.AppBar(title=ft.Text("Flet app")),
                    ft.ElevatedButton("Ir a configuración", on_click=open_settings)
                ]
            )
        )
        
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.AppBar(title=ft.Text("Settings"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Settings!", style="bodyMedium"),
                        ft.ElevatedButton("Go to mail settings", on_click=open_mail_settings),
                    ],
                )
            )
            
        if page.route == "/settings/mail":
            page.views.append(
                ft.View(
                    "/settings/mail",
                    [
                        ft.AppBar(
                            title=ft.Text("Mail Settings"), bgcolor=ft.colors.SURFACE_VARIANT
                        ),
                        ft.Text("Mail settings!"),
                    ],
                )
            )
            
        page.update()
        
    def view_pop(e):
        print("View pop", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    def open_mail_settings(e):
        page.go("/settings/mail")
        
    def open_settings(e):
        page.go("/settings")
    
    page.go(page.route)
        
ft.app(target=main)