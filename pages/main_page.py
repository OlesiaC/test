import allure
from playwright.sync_api import Page
from playwright.sync_api import expect

from pages.base_page import BasePage


class MainPage(BasePage):
    MODAL_WINDOW = "div.dy-modal-contents"
    MEMORIAL_DAY_BANNER_CLOSE = "div.dy-lb-close"
    MAIN_PAGE_TITLE = "Awara"
    HERO_BANNER = "div.hero-section-wrap_qAV"
    SHOP_AND_SAVE_BUTTON = "a[data-testid='hero_shop_mattress']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_url = self.HOST

    @allure.step("Close Memorial Day Sale banner")
    def close_memorial_day_banner(self) -> None:
        try:
            banner = self.page.locator(self.MODAL_WINDOW)
            close_button = banner.page.locator(self.MEMORIAL_DAY_BANNER_CLOSE)
            close_button.click()
            expect(banner, "Memorial Day Sale banner is not closed").not_to_be_visible()
        except Exception:
            print("Memorial Day Sale banner is not presented")
            pass

    @allure.step("Should be hero banner")
    def should_be_hero_banner(self) -> None:
        element = self.page.locator(self.HERO_BANNER)
        expect(element, "No hero banner presented").to_be_visible()

    @allure.step("Click Shop & Save” button")
    def click_shop_and_save_button(self) -> None:
        button = self.page.locator(self.SHOP_AND_SAVE_BUTTON)
        expect(button, "Shop & Save button is not presented").to_be_visible()
        button.click()

