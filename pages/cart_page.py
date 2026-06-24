from config import PlaywrightConfig
from playwright.sync_api import expect, Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self):
        self.page.goto(PlaywrightConfig.BASE_URL)
        self.page.locator("#user-name").fill("standard_user")
        self.page.locator("#password").fill("secret_sauce")
        self.page.locator("#login-button").click()
        self.page.wait_for_url("**/inventory.html")

    def add_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        self.page.locator("#add-to-cart-sauce-labs-bike-light").click()
        self.page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
        self.page.locator("#add-to-cart-sauce-labs-onesie").click()
        self.page.locator('[id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
        self.page.locator(".shopping_cart_link").click()
        self.page.wait_for_url("**/cart.html")
    
    def verify_cart(self):
        expect(self.page).to_have_url(f"{PlaywrightConfig.BASE_URL}cart.html")
        expect(self.page.locator(".cart_item")).to_have_count(6)
        
        expected_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]
        expect(self.page.locator(".inventory_item_name")).to_have_text(expected_items)
        print(expected_items)

    def verify_pageHeading(self):
        heading=self.page.get_by_test_id("secondary-header")    
        expect(heading).to_have_text("Your Cart")
        print("Cart page heading verified")

    def verify_Quantity(self):
        # verify total quantity
        quantities=self.page.locator(".shopping_cart_badge")
        
        #assert it
        expect(quantities).to_have_text("6")

    def verify_cartItems(self):
        item_names=self.page.locator(".inventory_item_name")
        expected_item_names=["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
        expect(item_names).to_have_text(expected_item_names)
        # assert count of all names
        expect(item_names).to_have_count(6)
        print(item_names.count())
    def verify_CheckoutButton(self):
        checkout=self.page.locator('#checkout')
        expect(checkout).to_be_visible(timeout=5000)
        print("Checkout button is visible")
        
    def verify_ContinueShoppingButton(self):
        ContinueShopping=self.page.locator('#continue-shopping')
        expect(ContinueShopping).to_be_visible(timeout=5000)
        print("Continue Shopping button is visible")

    def verify_RemoveButtons(self):
        RemoveButtons = self.page.locator(".cart_button")
        expect(RemoveButtons).to_have_count(6)
        print("All Remove buttons are visible")
        #print count
        print(RemoveButtons.count())

    def verify_RemoveItems(self):
        RemoveButtons = self.page.locator(".cart_button")
        RemoveButtons.first.click()
        expect(RemoveButtons).to_have_count(5)
        print(f"Remove buttons count is {RemoveButtons.count()}")