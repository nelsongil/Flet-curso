import flet as ft

def main(page:ft.Page):
    lvw_textos = ft.ListView(expand=True, spacing=10)
    
    for i in range(5000):
        lvw_textos.controls.append(ft.Text(f'Line {i}'))
        
    page.add(lvw_textos)
    

ft.app(target=main)