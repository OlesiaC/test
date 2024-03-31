import allure
from playwright.sync_api import Page, expect

from cfg.constants import UI_TEST_HOST


class BasePage:
    HOST = UI_TEST_HOST

    def __init__(self, page: Page, url: str = None):
        self.page: Page = page
        self.page_url = url

    def wait_for_stability(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("load")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    @allure.step("Open page")
    def open(self) -> None:
        self.page.goto(self.page_url)
        self.wait_for_stability()

    @allure.step("Check page title")
    def check_page_title(self, title: str) -> None:
        expect(self.page).to_have_title(title)

    @allure.step("Check page url")
    def check_page_url(self, url: str) -> None:
        expect(self.page).to_have_url(url)
