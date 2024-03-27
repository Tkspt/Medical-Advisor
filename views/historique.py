import flet as ft
from flet import *
from fletrt import Route
from db import conectedUser

class HistoriqueView(Route):
    def body(self):
        def se_deconnecter():            
            conectedUser.remove(conectedUser[0])
            self.go("/")
            
        first_page_contents = Container(
            content=Column(
                controls=[
                    Row(alignment='spaceBetween',
                        controls=[
                            Container(content=Icon(icons.MENU, color=ft.colors.GREEN_500)),
                            Row(controls=[
                                Text(conectedUser[0].first_name),
                                IconButton(
                                    icons.LOGOUT,
                                    icon_color=ft.colors.RED,
                                    on_click=lambda _: se_deconnecter(),
                                )
                            ]),
                        ],
                    ),

                    ft.SafeArea(
                        expand=True,
                        content=Column(
                            controls=[
                                Container(height = 10),
                                Row(
                                    alignment = MainAxisAlignment.CENTER,
                                    controls = [
                                        Text("Aucun historique de conversation trouvé !")
                                    ]
                                )                      
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
            width = 400,
            height = 850,
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
    
    def floating_action_button(self) -> FloatingActionButton:
        return ft.FloatingActionButton(
            icon=ft.icons.CHAT,
            bgcolor=ft.colors.GREEN_500,
            on_click=lambda _: self.go("/chat")
        )
    
    def view(self) -> View:
        view = super().view()
        return view