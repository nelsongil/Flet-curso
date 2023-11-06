import flet as ft

def main(page: ft.Page):
    lenguajes = ['Python', 'Flet', 'Flutter']
    etiquetas = []
    
    for e in lenguajes:
        etiquetas.append(ft.Text(e))
        
    row_datos = ft.Row(controls=etiquetas)
    
    page.add(row_datos)
    
    
    # Este era el contenido del main, formas distintas de crear controles
    """page.add(
        ft.Row(controls=[
            ft.Text("Python"),
            ft.Text("Flet"),
            ft.Text("Row")
        ])
    )"""

ft.app(target=main)