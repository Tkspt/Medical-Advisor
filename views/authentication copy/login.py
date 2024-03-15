import flet as ft

def login_page(page: ft.Page):
    # Définition des couleurs
    blanc = ft.colors.WHITE
    vert = ft.colors.GREEN
    noir = ft.colors.BLACK
    gris = ft.colors.BLUE_GREY
    page.bgcolor="white"

    # Ajout du titre de la page
    page.add(
        ft.Text("Page d'accueil", size=32, weight=ft.FontWeight.BOLD, color=noir)
    )

    # Ajout d'un bouton pour quitter l'application
    page.add(
        ft.ElevatedButton(text="Quitter", bgcolor=vert, color=blanc, on_click=lambda _: quitter(page))
    )

def quitter(page):
    page.update()
    page.dialog = ft.AlertDialog(
        title=ft.Text("Quitter"),
        content=ft.Text("Voulez-vous vraiment quitter l'application ?"),
        actions=[
            ft.ElevatedButton(text="Oui", on_click=lambda _: page.go("/")),
            ft.ElevatedButton(text="Non", on_click=lambda _: page.dialog.close()),
        ],
    )
    page.dialog.open = True