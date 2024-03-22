import flet as ft
from flet import *

""" def main(page: ft.Page):
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

ft.app(target=main, view=ft.WEB_BROWSER) """





def main(page: Page):

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(content=Icon(icons.MENU, color=ft.colors.GREEN_500)),
                        Row(controls=[
                            Icon(icons.SEARCH, color=ft.colors.GREEN_500),
                            Icon(icons.NOTIFICATION_ADD_OUTLINED,color=ft.colors.GREEN_500)
                        ]),
                    ],
                ),
                Container(height=60),

                ft.SafeArea(
                    expand=True,
                    content=ft.Column(
                        horizontal_alignment="center",
                        controls=[
                            ft.Divider(height=20, color="transparent"),
                            ft.Container(
                                bgcolor="white10",
                                width=150,
                                height=150,
                                shape=ft.BoxShape("circle"),
                                image_src="./logos/logo1.png",
                                image_fit="cover",
                                shadow=ft.BoxShadow(
                                    spread_radius=6,
                                    blur_radius=20,
                                    color=ft.colors.with_opacity(0.71, "Green"),
                                ),
                            ),
                            Container(height=40),
                            ft.Divider(height=20, color="Green500"),
                            ft.Text("Votre application de conseil Santé", size=20, color='black'),
                            ft.Divider(height=20, color="Green500"),

                            Container(height=30),
                            ft.ElevatedButton(text="Créer un compte", width=180, bgcolor="Green700", color="white", adaptive=
                                              True),
                            ft.ElevatedButton(text="Se Connecter", width=180, bgcolor="Green700", color="white", adaptive=True),
                        ]
                    )
                ),
            ]    
        )        
    )

    page_1 = Container()
    page_2 = Row(
    controls=[
        Container(
            width=400,
            height=850,
            bgcolor='white',
            border_radius=35,
            padding = padding.only(
                top=50, left=20,
                right=20,bottom=5
            ),
            content=Column(
                controls=[
                    first_page_contents
                ]
            )
        )
    ]
)
    container = Container(
        width=400,
        height=850,
        bgcolor='white',
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )
    page.add(container)

app(target=main)