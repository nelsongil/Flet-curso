import flet as ft

def main(page:ft.Page):
    
    def saludar_clicked(e):
        if not txt_nombre.value:
            txt_nombre.error_text = 'Por favor ingrese su nombre'
            page.update
        else:
            nombre = txt_nombre.value
            page.clean()
            lbl_text2 = ft.Text(
                spans=[
                    ft.TextSpan(
                        f"Hola {nombre}!",
                        ft.TextStyle(
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    (0, 20), (150, 20), [ft.colors.BLUE_500, ft.colors.INDIGO_800]
                                )
                            ),
                        ),
                    ),
                ],
            )
            page.add(lbl_text2)
        
    txt_nombre = ft.TextField(label="Su nombre")
    
    page.add(txt_nombre, ft.ElevatedButton("Di Hola", on_click=saludar_clicked))


ft.app(target=main)
