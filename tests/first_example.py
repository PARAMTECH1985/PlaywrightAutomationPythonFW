# test_playwright_homepage.py

import pytest
import os
from playwright.sync_api import Page, expect, sync_playwright

BASE_URL = "https://playwright.dev/python"


# ✅ Ensure screenshot directory exists
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    os.makedirs("screenshots", exist_ok=True)


# ✅ Open homepage fixture
@pytest.fixture(scope="function")
def open_home_page(page: Page):
    with sync_playwright() as p:  # Launch browser (headless=False lets you see the browser) browser = p.chromium.launch(headless=False) page = browser.new_page()
        # Launch browser (headless=False lets you see the browser)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="domcontentloaded")
        return page


# ✅ Test: Title (use partial match for stability)
def test_homepage_title(open_home_page: Page):
    expect(open_home_page).to_have_title(lambda title: "Playwright" in title)


# ✅ Test: URL validation
def test_homepage_url(open_home_page: Page):
    expect(open_home_page).to_have_url(BASE_URL)


# ✅ Test: Main heading visible (FIXED TEXT)
def test_homepage_heading_visible(open_home_page: Page):
    heading = open_home_page.get_by_role("heading", name="Playwright")
    expect(heading).to_be_visible()


# ✅ Test: Get Started link visible
def test_get_started_link_visible(open_home_page: Page):
    expect(open_home_page.get_by_role("link", name="Get started")).to_be_visible()


# ✅ Test: Click Get Started
def test_click_get_started(open_home_page: Page):
    open_home_page.get_by_role("link", name="Get started").click()
    expect(open_home_page).to_have_url("https://playwright.dev/python/docs/intro")


# ✅ Test: Search button visible
def test_search_button_visible(open_home_page: Page):
    expect(open_home_page.get_by_role("button", name="Search")).to_be_visible()


# ✅ Test: Screenshot
def test_take_homepage_screenshot(open_home_page: Page):
    open_home_page.screenshot(
        path="screenshots/playwright_homepage.png",
        full_page=True
    )