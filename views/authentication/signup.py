import flet as ft

def signup_page(page: ft.Page):
    # Définition des couleurs
    blanc = ft.colors.WHITE
    vert = ft.colors.GREEN
    noir = ft.colors.BLACK
    gris = ft.colors.BLUE_GREY
    page.bgcolor="white"

    # Création des champs de saisie
    champ_nom = ft.TextField(label="Nom", color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir))
    champ_prenom = ft.TextField(label="Prénom", color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir))
    champ_email = ft.TextField(label="Email", color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir))
    champ_sexe = ft.Dropdown(label="Sexe", width=200, color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir),
        options=[
            ft.dropdown.Option("Homme"),
            ft.dropdown.Option("Femme"),
            ft.dropdown.Option("Autre"),
        ],
    )
    champ_mot_de_passe = ft.TextField(label="Mot de passe", color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir), password=True)

    # Création des boutons
    bouton_creer_compte = ft.ElevatedButton(text="Créer un compte", bgcolor=vert, color=noir, on_click=lambda _: creer_compte(page))
    bouton_annuler = ft.ElevatedButton(text="Annuler", bgcolor=vert, color=noir, on_click=lambda _: annuler(page))

    # Ajout des champs de saisie et des boutons à la page
    page.add(
        ft.Column([
                ft.Row(
                    [
                        ft.Text("Nom", color=noir),
                        champ_nom,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    [
                        ft.Text("Prénom", color=noir),
                        champ_prenom,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    [
                        ft.Text("Email", color=noir),
                        champ_email,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    [
                        ft.Text("Sexe", color=noir),
                        champ_sexe,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    [
                        ft.Text("Mot de passe", color=noir),
                        champ_mot_de_passe,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    [
                        bouton_creer_compte,
                        bouton_annuler,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=10,
        ),
    )

def creer_compte(page):
    # Traiter les données saisies et créer le compte utilisateur
    # Rediriger vers la page d'accueil de l'application
    from views.home import home_page
    home_page(page)

def annuler(page):
    # Rediriger vers la page d'accueil de l'application
   from views.home import home_page
   home_page(page)