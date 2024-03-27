import flet as ft
from flet import *
from fletrt import Route
from utils.validation import Validation
from db import users
from entities.user import User

class SignupView(Route):                
    def body(self):
        global first_name, last_name, email, phone, password, password_confirm, cgu
        
        def s_inscrire():
            validator = Validation()
            error_message = None
            if not validator.is_valid_first_name(first_name.value):
                error_message = "Le prénom doit être au moins trois caractères"
                
            elif not validator.is_valid_last_name(last_name.value):
                error_message = "Le nom doit être au moins deux caractères"
                
            elif not email.value:
                error_message = "L'email est obligatoire"
                
            elif not phone.value:
                error_message = "Le numéro de téléphone est obligatoire"
                
            elif not validator.is_valid_password(password.value):
                error_message = "Le mot de passe doit être au moins 8 caractères et doit contenir au moins un chiffre"
                
            elif password_confirm.value != password.value:
                error_message = "Les deux mots de passe doivent être les mêmes"
                
            elif not cgu.value:
                error_message = "Veuillez accepter les conditions générales d'utilisation"
                
            foundUser = [us for us in users if us.email == email.value]
            if len(foundUser) > 0:
                error_message = "Cet email est dèjà utilisé"
                
            if(error_message != None):
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Text(error_message),
                    bgcolor = colors.RED_400,
                    action="OK",
                )
                self.page.snack_bar.open = True
                self.page.update()
            else:
                user = User(
                    len(users) + 1,
                    first_name.value,
                    last_name.value,
                    email.value,
                    phone.value,
                    password.value,
                    30
                )
                users.append(user)
                
                self.go("/login")
            
            self.page.update()
        
        first_name = ft.TextField(
            label="Prénom",
            width=300,
            color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            height = 40,
        )
        last_name = ft.TextField(
            label="Nom",
            width=300,
            color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            height = 40,
        )
        email = ft.TextField(
            label="Email",
            width=300,
            color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            height = 40,
        )
        phone = ft.TextField(
            label="Téléphone",
            width=300,
            color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            keyboard_type=ft.KeyboardType.PHONE,
            height = 40,
        )
        password = ft.TextField(
            label="Mot de Passe",
            password=True,
            can_reveal_password=True,
            width=300, color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            height = 40,
        )
        password_confirm = ft.TextField(
            label="Confirmer le mot de Passe",
            password=True,
            can_reveal_password=True,
            width=300, color='black',
            border_color='Green500',
            hint_style=ft.TextStyle(color='black'),
            height = 40,
        )
        cgu = ft.Checkbox(label = "J'accepte les CGU")
        
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

                    ft.SafeArea(
                        expand=True,
                        content=ft.Column(
                            expand = True,
                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment="center",
                            controls=[
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
                                ft.Text("Inscrivez-vous", size=20, color='black', weight = FontWeight.BOLD),
                                Container(height=10),
                                first_name,
                                last_name,
                                email,
                                phone,
                                password,
                                password_confirm,
                                Container(
                                    cgu,
                                    padding = padding.only(left = 45),
                                ),
                                Container(height=5),
                                ft.ElevatedButton(
                                    text="Créer mon compte",
                                    width=300,
                                    bgcolor="Green700", 
                                    height=40,
                                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)) ,
                                    color="white", 
                                    on_click=lambda _: s_inscrire()
                                ),
                                
                            ]
                        )
                    ),
                ]    
            )
        )
        first_page_contents

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