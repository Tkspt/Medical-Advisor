import flet as ft
from flet import *
from fletrt import Route

class SignupView(Route):
    def body(self):        
        first_page_contents = Container(
            content=Column(
                controls=[
                    Row(alignment='spaceBetween',
                        controls=[
                            Container(
                                content = IconButton(
                                    icons.ARROW_BACK,
                                    icon_color=ft.colors.GREEN_500,
                                    on_click=lambda _: self.go("/")
                                )
                            ),
                            Row(controls=[
                                Icon(icons.NOTIFICATION_ADD_OUTLINED,color=ft.colors.GREEN_500)
                            ]),
                        ],
                    ),
                    Container(height=5),

                    ft.SafeArea(
                        expand=True,
                        content=ft.Column(
                            horizontal_alignment="center",
                            controls=[
                                ft.Divider(height=20, color="transparent"),
                                ft.Container(
                                    bgcolor="white10",
                                    width=100,
                                    height=100,
                                    shape=ft.BoxShape("circle"),
                                    image_src="./logos/logo1.png",
                                    image_fit="cover",
                                    shadow=ft.BoxShadow(
                                        spread_radius=6,
                                        blur_radius=20,
                                        color=ft.colors.with_opacity(0.71, "Green"),
                                    ),
                                ),
                                Container(height=10),
                                ft.Text("Inscrivez-vous", size=20, color='black', weight = FontWeight.BOLD),
                                Container(height=10),
                                ft.TextField(
                                    label="Prénom",
                                    width=300,
                                    color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    height = 40,
                                ),
                                ft.TextField(
                                    label="Nom",
                                    width=300,
                                    color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    height = 40,
                                ),
                                ft.TextField(
                                    label="Email",
                                    width=300,
                                    color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    height = 40,
                                ),
                                ft.TextField(
                                    label="Téléphone",
                                    width=300,
                                    color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    keyboard_type=ft.KeyboardType.PHONE,
                                    height = 40,
                                ),
                                ft.TextField(
                                    label="Date",
                                    width=300,
                                    color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    keyboard_type=ft.KeyboardType.DATETIME,
                                    height = 40,
                                ),
                                ft.TextField(
                                    label="Mot de Passe",
                                    password=True,
                                    can_reveal_password=True,
                                    width=300, color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    height = 40,
                                ),
                                ft.TextField(
                                    label="Confirmer le mot de Passe",
                                    password=True,
                                    can_reveal_password=True,
                                    width=300, color='black',
                                    border_color='Green500',
                                    hint_style=ft.TextStyle(color='black'),
                                    height = 40,
                                ),
                                Container(
                                    ft.Checkbox(label = "J'accepte les CGU"),
                                    padding = padding.only(left = 23),
                                ),
                                Container(height=5),
                                ft.ElevatedButton(
                                    text="Créer mon compte",
                                    width=300,
                                    bgcolor="Green700", 
                                    height=40,
                                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)) ,
                                    color="white", 
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
        container = Container(
            width=400,
            bgcolor='white',
            border_radius=35,
            content=Stack(
                controls=[
                    page_1,
                    page_2
                ]
            )
        )
        return container
    
    def view(self) -> View:
        view = super().view()
        return view