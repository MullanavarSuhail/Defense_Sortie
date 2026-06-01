from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import *

def test_add_to_cart(page):
    page.goto(BASE_URL)
    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )

    inventory = InventoryPage(page)
    inventory.add_backpack()
    badge = page.locator(".shopping_cart_badge").inner_text()

    assert badge == "1"