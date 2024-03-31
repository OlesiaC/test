import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    """Fixture to launch and close the browser."""
    with sync_playwright() as p:
        # Check if DEBUG environment variable is set to 1
        headless = os.getenv('DEBUG') != '1'
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Fixture to create and close a new browser page for each test."""
    page = browser.new_page()
    yield page
    page.close()
