import allure
from playwright.sync_api import Page
from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    MODAL_WINDOW = "div[data-testid='popup_modal_dialog']"
    REJECT_OFFER_BUTTON = "//a[text()='No, Thanks']"
    ORDER_SUMMARY_ITEMS = "div[data-testid='cart_items_area']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_url = f"{self.HOST}/checkout/shipping"

    @allure.step("Close Awara extended banner")
    def close_awara_extended_banner(self) -> None:
        try:
            banner = self.page.locator(self.MODAL_WINDOW)
            close_button = banner.locator(self.REJECT_OFFER_BUTTON)
            close_button.click()
            expect(banner, "Awara extended banner is not closed").not_to_be_visible()
        except Exception:
            print("Awara extended banner is not presented")
            pass

    @allure.step("Check that item is added to the cart")
    def check_item_added_to_cart(self, item) -> None:
        order_summary = self.page.locator(self.ORDER_SUMMARY_ITEMS)
        item_in_cart = order_summary.locator(f"//a[text()='{item}']")
        expect(item_in_cart, "Item is not added to the cart").to_be_visible()
