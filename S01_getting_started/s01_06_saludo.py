import flet as ft

def main(page: ft.Page):
    page.window_width = 700        # window's width is 200 px
    page.window_height = 400       # window's height is 200 px
    page.window_resizable = False  # window is not resizable
    
    txtnombre=ft.TextField(label='Digite su nombe')
    lbl_saludo =ft.Text()

    def saludar(e):
        if not txtnombre.value:
            txtnombre.error_text = "Please enter your name"
            txtnombre.update()
        else:
            name = txtnombre.value
            lbl_saludo.value = f"Hello, {name}!"
            page.update()
    
    
    row = ft.Row(controls=[
        txtnombre,
        ft.ElevatedButton(text='Saludar', on_click=saludar),
        lbl_saludo
    ])

    page.add(row)
               
ft.app(target=main, assets_dir="assets")