import pytest
from playwright.sync_api import Page
from pages.Dashboard_page import DashboardPage


class TestDashboard:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Runs before every test — initializes DashboardPage and navigates once."""
        self.dashboard_page = DashboardPage(page)
        self.dashboard_page.navigate()

    def test_dashboard(self):
        self.dashboard_page.verify_page_title()
        print("Dashboard page title verified")

    def test_verify_FilterDropdonOptions(self):
        self.dashboard_page.verify_FilterDropdonOptions()
        print("Filter Dropdown Options verified")

    def test_verify_navigationMenu(self):
        self.dashboard_page.verify_navigationMenu()
        print("Navigation Menu verified")

    def test_verify_Products(self):
        self.dashboard_page.verify_Products()
    def test_verify_prices(self):
        self.dashboard_page.verify_prices()
    def test_verify_menu_text_hoverColor(self):
        self.dashboard_page.verify_menu_text_hoverColor()
        print("Navigation Menu hover color verified")