
import time

from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError,
)

from pages.locators import TeamsSignLocators


class TeamsSign:

    def __init__(self, timeout=60):
        self.teams = TeamsSignLocators()
        self.timeout = timeout

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def open_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False, args=["--start-maximized"]
        )
        self.context = self.browser.new_context(no_viewport=True)
        self.page = self.context.new_page()
        self.page.set_default_timeout(self.timeout * 1000)

        self.page.goto(self.teams.LOGIN_URL)

    def _switch_to_login_window(self):
        """Find the page containing the email field."""
        deadline = time.monotonic() + self.timeout

        while time.monotonic() < deadline:
            for page in self.context.pages:
                try:
                    page.locator(
                        self.teams.EMAIL_INPUT
                    ).wait_for(state="visible", timeout=1000)

                    self.page = page
                    return
                except PlaywrightTimeoutError:
                    continue

            time.sleep(0.5)

        raise TimeoutError("Login email field was not found")

    def sign_in_teams(self):
        self.page.locator(self.teams.SIGN_IN_BTN).first.click()
        self._switch_to_login_window()

    def send_email_id(self, email_address):
        field = self.page.locator(self.teams.EMAIL_INPUT).first
        field.wait_for(state="visible")
        field.fill(email_address)

        assert field.input_value() == email_address, (
            "Email was not entered"
        )

        self.page.locator(self.teams.NEXT_BTN_1).click()

    def enter_email_password(self, password):
        use_password = self.page.locator(self.teams.USE_YOUR_PASSWORD).first
        password_field = self.page.locator(self.teams.PASSWORD_INPUT)

        # Wait for either the verify screen or the password box
        use_password.or_(password_field).first.wait_for(state="visible", timeout=15000)

        if use_password.is_visible():
            use_password.click()

        password_field.wait_for(state="visible", timeout=10000)
        password_field.fill(password)

        self.page.locator(self.teams.NEXT_BTN_2).click()

        no_button = self.page.locator(self.teams.NO_BUTTON)
        try:
            no_button.wait_for(state="visible", timeout=10000)
            no_button.click()
        except PlaywrightTimeoutError:
            pass
        time.sleep(20)

    def click_chat_button(self):
        self.page.locator(
            self.teams.CHAT_BUTTON
        ).click()
        time.sleep(20)

    def click_meet_button(self):
        self.page.locator(
            self.teams.MEET_BUTTON
        ).click()
        time.sleep(20)

    def click_people_button(self):
        self.page.locator(
            self.teams.PEOPLE_BUTTON
        ).click()
        time.sleep(20)

    def click_copilot_button(self):
        self.page.locator(
            self.teams.COPILOT_BUTTON
        ).click()
        time.sleep(20)

    def click_communities_button(self):
        self.page.locator(
            self.teams.COMMUNITIES_BUTTON
        ).click()
        time.sleep(20)

    def click_activity_button(self):
        self.page.locator(
            self.teams.ACTIVITY_BUTTON
        ).click()
        time.sleep(20)

    def click_calender_button(self):
        self.page.locator(
            self.teams.CALENDAR_BUTTON
        ).click()
        time.sleep(20)

        self.page.locator(
            self.teams.NEW_MEETING_BUTTON
        ).click()
        time.sleep(20)

        # This assumes the meeting form is ready to save.
        self.page.locator(
            self.teams.SAVE_BUTTON
        ).click()
        time.sleep(20)

    def close_browser(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()


# if __name__ == "__main__":
#     teams = TeamsSign()
#     teams.open_browser()
#     teams.sign_in_teams()
#     teams.send_email_id("starlocktemp@outlook.com")
#     teams.enter_email_password("rakesh@1234")
#     teams.click_chat_button()
#     teams.click_meet_button()
#     teams.click_people_button()
#     teams.click_copilot_button()
#     teams.click_communities_button()
#     teams.click_activity_button()
#     teams.click_calender_button()
#     teams.close_browser()

