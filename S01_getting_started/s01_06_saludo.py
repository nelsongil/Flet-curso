import flet as ft

def main(page: ft.Page):
    page.window_width = 500        # window's width is 200 px
    page.window_height = 400       # window's height is 200 px
    page.window_resizable = False  # window is not resizable

    def saludar(e):
        if not txtnombre.value:
            txtnombre.error_text = "Please enter your name"
            page.update()
        else:
            name = txtnombre.value
            page.add(ft.Text(f"Hello, {name}!")) 
    
    txtnombre=ft.TextField
    
    row = ft.Row(controls=[
        txtnombre(label='Digite su nombe'),
        ft.ElevatedButton(text='Saludar', on_click=saludar)
    ])

    page.add(row)
               
ft.app(target=main, assets_dir="assets")