from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import *

def test_inventory(page):
    page.goto(BASE_URL)

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )

    products = page.locator(".inventory_item").count()

    assert products == 6