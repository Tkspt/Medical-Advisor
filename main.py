import flet as ft

def main(page: ft.Page):
    # Définition des couleurs
    blanc = ft.colors.WHITE
    vert = ft.colors.GREEN
    noir = ft.colors.BLACK
    gris = ft.colors.BLUE_GREY
    page.bgcolor="white"

    # Ajout du titre de la page
    page.add(
        ft.Text("Page de connexion", size=32, weight=ft.FontWeight.BOLD, color=noir)
    )

    # Ajout des boutons pour se connecter et créer un compte
    page.add(
        ft.Row(
            [
                ft.ElevatedButton(text="Se connecter", bgcolor=vert, color=blanc, on_click=lambda _: home_page(page)),
                ft.ElevatedButton(text="Créer un compte", bgcolor=vert, color=blanc, on_click=lambda _: signup_page(page)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

def home_page(page):
    from views.home import home_page
    home_page(page)

def signup_page(page):
    from views.authentication.signup import signup_page
    signup_page(page)

ft.app(target=main, view=ft.WEB_BROWSER)