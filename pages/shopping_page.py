import allure
from playwright.sync_api import Page
from playwright.sync_api import expect

from pages.base_page import BasePage


class ShoppingPage(BasePage):
    SHOP_ITEM_HEADER = "h1"
    ADD_TO_CART_BUTTON = "button[data-testid='addtocart_btn']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_url = f"{self.HOST}/premier-mattress"

    @allure.step("Check shopping item header")
    def check_shopping_item_header(self, text) -> None:
        element = self.page.locator(self.SHOP_ITEM_HEADER)
        expect(element, "No shopping item header presented").to_be_visible()
        expect(element).to_have_text(text)

    @allure.step("Add item to cart")
    def add_item_to_cart(self) -> None:
        button = self.page.locator(self.ADD_TO_CART_BUTTON)
        expect(button, "Add to cart button is not presented").to_be_visible()
        button.click()
