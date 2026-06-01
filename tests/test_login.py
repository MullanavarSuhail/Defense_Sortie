from pages.login_page import LoginPage
from utils.config import *

def test_login(page):
    page.goto(BASE_URL)

    login = LoginPage(page)

    login.login(
        USERNAME,
        PASSWORD
    )

    assert "inventory" in page.url