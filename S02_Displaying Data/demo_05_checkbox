import flet as ft

def main(page:ft.Page):
    def submint_clicked(e):
        lbl_resultado.value = f'El valor del Dropdown es: {cbx_color.value}'
        page.update()
    
    lbl_resultado = ft.Text()
    
    btn_submit = ft.ElevatedButton(text='Enviar', on_click=submint_clicked)
    
    cbx_color = ft.Dropdown(
        label='Colores',
        hint_text="Choose your favourite color?",
        options= [
            ft.dropdown.Option('Rojo'),
            ft.dropdown.Option('Verde'),
            ft.dropdown.Option('Azul')
        ]
    )
    page.add(cbx_color, btn_submit, lbl_resultado)

ft.app(target=main)