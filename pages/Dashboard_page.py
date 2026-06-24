from config import PlaywrightConfig
from playwright.sync_api import expect, Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        # Login is required; direct navigation to /inventory.html redirects to login page
        self.page.goto(PlaywrightConfig.BASE_URL)
        self.page.locator("#user-name").fill("standard_user")
        self.page.locator("#password").fill("secret_sauce")
        self.page.locator("#login-button").click()
        self.page.wait_for_url("**/inventory.html")

    def verify_page_title(self):
        expect(self.page).to_have_title("Swag Labs")

    def verify_FilterDropdonOptions(self):
        # The sort dropdown is a <select class="product_sort_container">
        # with exactly 4 <option> children
        options = self.page.locator("select.product_sort_container option")
        expect(options).to_have_count(4)

        # Verify the option labels
        expected_options = [
            "Name (A to Z)",
            "Name (Z to A)",
            "Price (low to high)",
            "Price (high to low)"
        ]
        for i, label in enumerate(expected_options):
            expect(options.nth(i)).to_have_text(label)
            print(f"  Option {i + 1}: {label}")
        print("Filter Dropdown Options verified")
    def verify_navigationMenu(self):
        nav_menu=self.page.locator("div.bm-burger-button")
        expect(nav_menu).to_be_visible()
        nav_menu.click()
        print("Navigation Menu verified")

    def verify_Products(self):
        products = self.page.locator("div.inventory_item")
        expect(products).to_have_count(6)
        # iterate product names
        product_names = self.page.locator("div.inventory_item_name")
        for i in range(products.count()):
            print(product_names.nth(i).text_content())
        
    def verify_prices(self):
        prices = self.page.locator("div.inventory_item_price")
        expect(prices).to_have_count(6)
        # iterate product prices
        for i in range(prices.count()):
            print(prices.nth(i).text_content())
        print("Prices verified")
        # print count of products
        print("Count of products: ", prices.count())
        
    def verify_DashboardPage_title(self):
        title=self.page.locator("span.title")
        expect(title).to_have_text("Swag Labs")
        print("Dashboard page title verified")

    def verify_menu_text_hoverColor(self):
        nav_menu = self.page.locator("#react-burger-menu-btn")
        expect(nav_menu).to_be_visible()
        nav_menu.click()
        print("Navigation Menu opened")

        # All sidebar nav links with their display names
        nav_links = [
            (self.page.locator("#inventory_sidebar_link"), "All Items"),
            (self.page.locator("#about_sidebar_link"),     "About"),
            (self.page.locator("#logout_sidebar_link"),    "Logout"),
            (self.page.locator("#reset_sidebar_link"),     "Reset App State"),
        ]

        # Hover color applied by the site's CSS: rgb(61, 220, 145) i.e. #3DDC91
        expected_hover_color = "rgb(61, 220, 145)"

        for locator, name in nav_links:
            locator.hover()
            expect(locator).to_have_css("color", expected_hover_color)
            print(f"  [PASS] '{name}' hover color verified: {expected_hover_color}")

        print("All Navigation Menu Link text hover colors verified")
