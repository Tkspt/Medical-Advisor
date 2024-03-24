import flet as ft
from flet import *

def login_page(page: ft.Page):
    
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
                            
                            Container(height=30),
                            ft.TextField(label="Email", width=300, color='black', border_color='Green500', hint_style=ft.TextStyle(color='black'), adaptive=True),
                            ft.TextField(label="Mot de Passe", password=True, can_reveal_password=True, width=300, color='black', border_color='Green500', hint_style=ft.TextStyle(color='black'), adaptive=True),
                            Container(height=10),
                            ft.ElevatedButton(
                                text="Se Connecter", 
                                width=300, bgcolor="Green700", 
                                height=50,
                                style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)) ,
                                color="white", 
                                adaptive=True, 
                                on_click=lambda _: login_page(page)
                            ),
                            
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
                top=30, left=20,
                right=20,bottom=5
            ),
            content=Column(
                controls=[
                    first_page_contents
                ]
            ),
            
        )
    ]
)
    container = Container(adaptive=True,
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