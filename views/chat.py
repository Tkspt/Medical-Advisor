import flet as ft
from flet import *
from fletrt import Route
from datetime import date
from db import chats
from db import messages
from db import conectedUser
from models.pathology import predire_maladie
from entities.message import Message
from entities.chat import Chat

class ChatView(Route):
    def body(self):
        global question
        
        def getTodaysChat():
            today = date.today()
            result = [ct for ct in chats if (ct.date == today and ct.userId == conectedUser[0].id)]
            if len(result) > 0:
                chat = result[0]
                msgs = [msg for msg in messages if (msg.chatId == chat.id)]
                return msgs
            else:
                return []
        
        def make_prediction():
            today = date.today()
            result = [ct for ct in chats if (ct.date == today)]
            chat = None
            
            if len(result) > 0:
                chat = result[0]
                new_msg = Message(len(messages) + 1, question.value, chat.id, today)
                messages.append(new_msg)
                # self.go("/historique")
            else:
                chat = Chat(len(chats) + 1, question.value, conectedUser[0].id, today)
                chats.append(chat)
                
                new_msg = Message(len(messages) + 1, question.value, chat.id, today)
                messages.append(new_msg)
                
            predicted_result = predire_maladie(question.value)
            new_msg = Message(len(messages) + 1, predicted_result, chat.id, today)
            messages.append(new_msg)
            
            [print(msg.label) for msg in messages]
        
        question = ft.TextField(
            expand = True,
            label="Posez votre question ici ...",
            color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            height = 40,
        )
        
        userChat = getTodaysChat()
        
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
                                            question,
                                            IconButton(
                                                icon = icons.SEND,
                                                icon_color= ft.colors.GREEN_500,
                                                on_click=lambda _: make_prediction(),
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