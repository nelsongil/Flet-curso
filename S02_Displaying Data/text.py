import flet as ft

def main(page: ft.Page):
    lbl_text = ft.Text( 
        value='Flet y Python',
        size=30,
        color='blue',
        weight='bold',
        italic=True
    )
    
    lbl_text2 = ft.Text(
        spans=[
            ft.TextSpan(
                "Greetings, planet!",
                ft.TextStyle(
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 20), (150, 20), [ft.colors.RED, ft.colors.YELLOW]
                        )
                    ),
                ),
            ),
        ],
    )
    
    lbl_text3 = ft.Container(
        padding=5,
        content=ft.Stack(
            height=100,
            width=400,
            controls=
            [
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Greetings, planet!",
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                foreground=ft.Paint(
                                    color=ft.colors.BLUE_700,
                                    stroke_width=6,
                                    stroke_join=ft.StrokeJoin.ROUND,
                                    style=ft.PaintingStyle.STROKE,
                                ),
                            ),
                        ),
                    ],
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Greetings, planet!",
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.GREY_300,
                            ),
                        ),
                    ],
                ),
            ]
        ))
    
    page.add(lbl_text, lbl_text2, lbl_text3)
    
ft.app(target=main)