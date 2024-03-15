# import flet as ft

# def home(page: ft.Page):
#     # Définition des couleurs
#     blanc = ft.colors.WHITE
#     vert = ft.colors.GREEN
#     noir = ft.colors.BLACK
#     gris = ft.colors.BLUE_GREY
#     page.bgcolor="white"

#     # Création des champs de saisie
#     champ_email = ft.TextField(label="Email", color=blanc, border_color=gris, hint_style=ft.TextStyle(color=noir))
#     champ_mot_de_passe = ft.TextField(label="Mot de passe", color=blanc, border_color=gris, hint_style=ft.TextStyle(color=noir), password=True)

#     # Création des boutons
#     bouton_se_connecter = ft.ElevatedButton(text="Se connecter", bgcolor=vert, color=blanc, on_click=lambda _: se_connecter(page))
#     bouton_creer_compte = ft.ElevatedButton(text="Créer un compte", bgcolor=vert, color=blanc, on_click=lambda _: creer_compte(page))

#     # Ajout des champs de saisie et des boutons à la page
#     page.add(
#         ft.Column(
#             [
#                 ft.Row(
#                     [
#                         ft.Text("Email", color=noir),
#                         champ_email,
#                     ],
#                     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                 ),
#                 ft.Row(
#                     [
#                         ft.Text("Mot de passe", color=noir),
#                         champ_mot_de_passe,
#                     ],
#                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                 ),
#                 ft.Row(
#                     [
#                         bouton_se_connecter,
#                         bouton_creer_compte,
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,
#                 ),
#             ],
#             spacing=10,
#         ),
#     )

# def se_connecter(page):
#     page.dialog = ft.AlertDialog(
#         title=ft.Text("Se connecter"),
#         content=ft.Text("Vous êtes maintenant connecté(e) !"),
#         actions=[
#             ft.ElevatedButton(text="OK", on_click=lambda _: page.dialog.close()),
#         ],
#     )
#     page.dialog.open = True

# def creer_compte(page):
#     page.dialog = ft.AlertDialog(
#         title=ft.Text("Créer un compte"),
#         content=ft.Text("Votre compte a été créé avec succès !"),
#         actions=[
#             ft.ElevatedButton(text="OK", on_click=lambda _: page.dialog.close()),
#         ],
#     )
#     page.dialog.open = True

# ft.app(target=home, view=ft.WEB_BROWSER)

import flet as ft

def home_page(page: ft.Page):
    # Définition des couleurs
    blanc = ft.colors.WHITE
    vert = ft.colors.GREEN
    noir = ft.colors.BLACK
    gris = ft.colors.BLUE_GREY
    page.bgcolor="white"

    # Création des champs de saisie
    champ_email = ft.TextField(label="Email", color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir))
    champ_mot_de_passe = ft.TextField(label="Mot de passe", color=noir, border_color=gris, hint_style=ft.TextStyle(color=noir), password=True)

    # Création des boutons
    bouton_se_connecter = ft.ElevatedButton(text="Se connecter", bgcolor=vert, color=noir, on_click=lambda _: se_connecter(page, champ_email.value, champ_mot_de_passe.value))
    bouton_creer_compte = ft.ElevatedButton(text="Créer un compte", bgcolor=vert, color=noir, on_click=lambda _: creer_compte(page))

    # Ajout des champs de saisie et des boutons à la page
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Email", color=noir),
                        champ_email,
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
                        bouton_se_connecter,
                        bouton_creer_compte,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=10,
        ),
    )

def se_connecter(page, email, mot_de_passe):
    if email and mot_de_passe:
        # Rediriger vers la page d'accueil de l'application
        from views.authentication.login import login_page
        login_page(page, email, mot_de_passe)

def creer_compte(page):
    from views.authentication.signup import signup_page
    signup_page(page)