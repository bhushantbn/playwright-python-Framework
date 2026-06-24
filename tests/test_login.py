import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Runs before every test — initializes LoginPage and navigates once."""
        self.login_page = LoginPage(page)
        self.page = page
        self.login_page.navigate()

    def test_successful_login(self):
        # Act
        self.login_page.login("standard_user", "secret_sauce")

        # Assert
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        print("Login successful")

    def test_invalid_login(self):
        # Act
        self.login_page.login("invalid_user", "invalid_password")

        # Assert
        expect(self.page).to_have_url("https://www.saucedemo.com/")
        error_message = self.page.locator(".error-message-container.error")
        expect(error_message).to_be_visible()
        expect(error_message).to_contain_text(
            "Epic sadface: Username and password do not match any user in this service"
        )
        print("Invalid login verified")

    def test_verify_close_icon(self):
        self.login_page.login("invalid_user", "invalid_password")
        close_icons = self.page.locator('[data-icon="times-circle"]')
        expect(close_icons).to_have_count(2)
        print("Close icon verified")
