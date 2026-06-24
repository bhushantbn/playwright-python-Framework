import pytest
from playwright.sync_api import Page
from pages.cart_page import CartPage
from pages.login_page import LoginPage


class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Runs before every test — initializes CartPage and navigates once."""
        self.cart_page = CartPage(page)
        self.page = page
        self.cart_page.navigate()
        self.cart_page.add_to_cart()

    def test_verify_cart(self):
        self.cart_page.verify_cart()
        print("Cart items verified")
    def test_verify_pageHeading(self):
        self.cart_page.verify_pageHeading()
        print("page heading is verified")
    def test_verify_Quantity(self):
        self.cart_page.verify_Quantity()
        print("Quantity verified")
    def test_verify_cartItems(self):
        self.cart_page.verify_cartItems()
        print("Cart items verified")
    def test_verify_CheckoutButton(self):
        self.cart_page.verify_CheckoutButton()
        print("Checkout button verified")
    def test_verify_ContinueShoppingButton(self):
        self.cart_page.verify_ContinueShoppingButton()
        print("Continue Shopping button verified")
    def test_verify_RemoveButtons(self):
        self.cart_page.verify_RemoveButtons()
        print("Remove buttons verified")
    def test_verify_RemoveItems(self):
        self.cart_page.verify_RemoveItems()
        print("Remove items verified")