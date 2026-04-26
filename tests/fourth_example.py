import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    # Navigate to the Playwright website
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the 'Get started' link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name 'Installation'.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
