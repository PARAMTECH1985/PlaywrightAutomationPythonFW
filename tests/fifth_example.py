import pytest
from playwright.sync_api import Page, expect


def test_user_registration(page: Page):
    # 1. Navigate to the signup page
    page.goto("https://demo.mediacms.io/accounts/signup/")

    # 2. Fill in registration details
    page.get_by_label("Username").fill("testuser_123")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Password").fill("SecurePass123!")
    page.get_by_label("Confirm Password").fill("SecurePass123!")

    # 3. Submit the form
    page.get_by_role("button", name="Register").click()

    # 4. Verify successful registration (e.g., URL change or success text)
    expect(page).to_have_url("https://mediacms.io")
