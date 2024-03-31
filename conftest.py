import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    """Fixture to launch and close the browser."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Fixture to create and close a new browser page for each test."""
    page = browser.new_page()
    yield page
    page.close()
