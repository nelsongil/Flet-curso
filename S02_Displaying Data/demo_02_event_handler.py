import flet as ft

def main(page: ft.Page):
    page.title= 'Contador'
    # Alineación Vertical _______________________________
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_numero = ft.TextField(value='0', text_align=ft.TextAlign.RIGHT, width=100)
    
    def reducir_clicked(e):
        txt_numero.value = str(int(txt_numero.value) - 1)        
        page.update()
        
    def aumentar_clicked(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.REMOVE_CIRCLE_OUTLINED,
                    icon_color=ft.colors.RED_400,
                    icon_size=40,
                    tooltip="Restar",
                    on_click=reducir_clicked,
                ),
                txt_numero,
                ft.IconButton(
                    icon=ft.icons.ADD_CIRCLE_OUTLINED,
                    icon_color=ft.colors.GREEN_500,
                    icon_size=40,
                    tooltip="Aumentar",
                    on_click=aumentar_clicked,
                ),
            ],
            
            # Alineación Horizontal _____________
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
ft.app(target=main)