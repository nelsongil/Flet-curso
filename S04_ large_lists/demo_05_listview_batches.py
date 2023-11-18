import flet as ft

def main(page:ft.Page):
     lvw_textos = ft.ListView(expand=1, spacing=10, item_extent=50)
     page.add(lvw_textos)
     
     for i in range(5100):
         lvw_textos.controls.append(ft.Text(f"Line {i}"))
         
         if i % 500 == 0:
             page.update()
    
ft.app(target=main)