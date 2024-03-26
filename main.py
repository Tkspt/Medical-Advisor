import flet as ft
from flet import *
from fletrt import Router
from views.home import HomeView
from views.authentication.login import LoginView
from views.authentication.signup import SignupView
from views.historique import HistoriqueView
from views.chat import ChatView

def main(page: Page):
    
    router = Router(
        page=page,
        routes={
            '/': HomeView(),
            '/login': LoginView(),
            '/signup': SignupView(),
            '/historique': HistoriqueView(),
            '/chat': ChatView(),
        },
        redirect_not_found=False,
    )

    router.install()

app(target=main)