import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage
from pages.shopping_page import ShoppingPage
from pages.cart_page import CartPage


class UITest:
    main_page: MainPage
    shopping_page = ShoppingPage
    cart_page = CartPage

    def init_pages(self, page: Page):
        self.main_page = MainPage(page)
        self.shopping_page = ShoppingPage(page)
        self.cart_page = CartPage(page)

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.init_pages(page)
