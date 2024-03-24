import flet as ft
from flet import *
from views.home import home_page
from views.authentication.login import login_page

def main(page: Page):
    # home_page(page)
    login_page(page)

app(target=main)