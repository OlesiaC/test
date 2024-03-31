import allure
import pytest

from tests.ui import UITest


@allure.epic("Awara Mattress")
@allure.suite("Hero banner flow")
class TestPurchase(UITest):

    @allure.title("Add item to cart")
    @pytest.mark.ui
    @pytest.mark.regression
    def test_add_item_to_cart(self):
        item_name = "Awara Premier Natural Hybrid Mattress"
        self.main_page.open()
        self.main_page.close_memorial_day_banner()
        self.main_page.check_page_title(self.main_page.MAIN_PAGE_TITLE)
        self.main_page.should_be_hero_banner()
        self.main_page.click_shop_and_save_button()
        self.shopping_page.check_page_url(self.shopping_page.page_url)
        self.shopping_page.check_shopping_item_header(item_name)
        self.shopping_page.add_item_to_cart()
        self.cart_page.close_awara_extended_banner()
        self.cart_page.check_item_added_to_cart(item_name)
