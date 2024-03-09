import flet as ft

def home(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Text(
            "Hello World 1 !",
            size=50,
            weight=ft.FontWeight.BOLD,
        ),
    )
    
ft.app(target=home)