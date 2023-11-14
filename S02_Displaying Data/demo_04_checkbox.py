import flet as ft

def main(page:ft.Page):
    def tarea_checked(e):
        lbl_resultado.value = (f'Has aprendido a programar! {chk_tarea.value}')
        
        page.update()
        
    lbl_resultado=ft.Text()
    chk_tarea=ft.Checkbox(label='Aprender a programar', value=False, on_change=tarea_checked)
    chk_tarea.fill_color={
    ft.MaterialState.HOVERED: ft.colors.GREEN,
    ft.MaterialState.FOCUSED: ft.colors.BLUE,  
    ft.MaterialState.DEFAULT: ft.colors.WHITE,
}
    
    page.add(chk_tarea,lbl_resultado)
    
ft.app(target=main)