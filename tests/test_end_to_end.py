from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import *

def test_end_to_end(page):

    page.goto(BASE_URL)

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )

    InventoryPage(page).add_backpack()

    InventoryPage(page).open_cart()

    CartPage(page).checkout()

    checkout = CheckoutPage(page)

    checkout.fill_information(
        "Suhail",
        "Mullanavar",
        "560037"
    )

    checkout.finish_order()

    assert "checkout-complete" in page.url