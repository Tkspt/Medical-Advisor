import flet as ft
from flet import *
from fletrt import Route

class ChatView(Route):
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
                                    on_click=lambda _: self.go('/historique')
                                )
                            ),
                            Row(controls=[
                                Icon(icons.NOTIFICATION_ADD_OUTLINED,color=ft.colors.GREEN_500)
                            ]),
                        ],
                    ),

                    ft.SafeArea(
                        expand = True,
                        content = Column(
                            expand = True,
                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                            controls = [
                                Container(
                                    expand = True,
                                    margin = margin.symmetric(vertical = 10),
                                    content = Column(
                                        alignment = MainAxisAlignment.START,
                                        controls = [
                                            Row(
                                                alignment = MainAxisAlignment.START,
                                                vertical_alignment = CrossAxisAlignment.START,
                                                controls = [
                                                    Container(
                                                        height = 30,
                                                        width = 30,
                                                        shape = BoxShape.CIRCLE,
                                                        bgcolor = colors.GREEN_500,
                                                        content = Icon(icons.PERSON, color=ft.colors.WHITE)
                                                    ),
                                                    Container(
                                                        expand = True,
                                                        content = Text(
                                                            "Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question Ceci est ma première question ",
                                                            text_align = TextAlign.JUSTIFY,
                                                        )
                                                    )
                                                ]
                                            ),
                                            Row(
                                                alignment = MainAxisAlignment.END,
                                                controls = [
                                                    Container(
                                                        expand = True,
                                                        bgcolor = colors.GREY_200,
                                                        padding = padding.symmetric(vertical = 10, horizontal = 5),
                                                        content = Text(
                                                            "Yeup !! et voici ta réponse Yeup !! et voici ta réponse Yeup !! et voici ta réponse Yeup !! et voici ta réponse Yeup !! et voici ta réponse Yeup !! et voici ta réponse Yeup !! et voici ta réponse",
                                                            text_align = TextAlign.RIGHT
                                                        ),
                                                        border_radius = 5,
                                                    )
                                                ]
                                            ),
                                        ]
                                    )
                                ),
                                Container(
                                    content = Row(
                                        expand = True,
                                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                                        controls = [
                                            ft.TextField(
                                                expand = True,
                                                label="Posez votre question ici ...",
                                                color='black',
                                                border_color='Green500',
                                                hint_style=ft.TextStyle(color='black'),
                                                height = 40,
                                            ),
                                            IconButton(
                                                icon = icons.SEND,
                                                icon_color= ft.colors.GREEN_500,
                                            )                    
                                        ]
                                    ),
                                ), 
                            ]
                        )                   
                    ),
                ]    
            )        
        )

        container = Container(
            expand = True,
            width = 400,
            bgcolor = 'white',
            content = first_page_contents
        )
        return container
    
    def view(self) -> View:
        view = super().view()
        return view