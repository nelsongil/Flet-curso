import flet as ft

def main(page: ft.Page):
    page.window_width = 500        # window's width is 200 px
    page.window_height = 400       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    txtnombre=ft.TextField(label='Digite su nombe')


    def saludar(e):
        if not txtnombre.value:
            txtnombre.error_text = "Please enter your name"
            txtnombre.update()
        else:
            name = txtnombre.value
            page.add(ft.Text(f"Hello, {name}!")) 
    
    
    row = ft.Row(controls=[
        txtnombre,
        ft.ElevatedButton(text='Saludar', on_click=saludar)
    ])

    page.add(row)
               
ft.app(target=main, assets_dir="assets")