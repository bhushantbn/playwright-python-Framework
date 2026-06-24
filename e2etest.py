from playwright.sync_api import sync_playwright, expect
import random


def test_e2e_shopping_flow():

    user = {
        "email": "standard_user",
        "password": "secret_sauce"
    }

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        # Open website
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", user["email"])

        page.fill("#password", user["password"])

        page.click("#login-button")

        print("Login successful")

        # Product list
        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie"
        ]

        # Random product selection
        selected_product = random.choice(products)

        print(f"Selected Product: {selected_product}")


        # Click selected product
        page.click(f"text={selected_product}")

        print(f"Product selected: {selected_product}")
        
        # add price verification
        price_locator = page.locator(f"text={selected_product}").locator("..").locator("div.inventory_details_price")
        product_price = price_locator.text_content()

        print(f"{selected_product} Product Price is: {product_price}")

        # Add to cart
        page.click("button:has-text('Add to cart')")

        print(f"{selected_product} added to cart")

        # Go to cart
        page.click(".shopping_cart_link")

        # Checkout
        page.click("#checkout")

        # Fill checkout details
        page.fill("#first-name", "Bhushan")

        page.fill("#last-name", "Trivedi")

        page.fill("#postal-code", "364001")

        page.click("#continue")

        # Finish order
        page.click("#finish")

        # Verify success message
        success_message = page.locator(".complete-header").text_content()

        assert success_message == "Thank you for your order!"

        print("E2E Test Passed")

        browser.close()

def test_verify_upgrade_prime_link():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        # Open website
        page.goto("https://www.amazon.in/")
        primemenu=page.locator("#nav-link-amazonprime")
        primemenu.hover()
        print("hovered on prime menu")

        upgrade_link = page.get_by_role("link", name="Join Prime Now")  
        expect(upgrade_link).to_be_visible(timeout=5000)
        print("Upgrade to Prime link is visible on the page.")

        upgrade_link.click()

        browser.close()