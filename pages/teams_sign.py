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

            self.page.wait_for_timeout(500)

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

        # Dynamically wait for the post-login dashboard navigation to be ready
        nav_button = (
            self.page.locator(self.teams.ACTIVITY_BUTTON)
            .or_(self.page.locator(self.teams.CHAT_BUTTON))
            .or_(self.page.locator(self.teams.CALENDAR_BUTTON))
        )
        try:
            nav_button.first.wait_for(state="visible", timeout=self.timeout * 1000)
        except PlaywrightTimeoutError:
            self.page.wait_for_load_state("domcontentloaded")

    def click_chat_button(self):
        chat_btn = self.page.locator(self.teams.CHAT_BUTTON)
        chat_btn.wait_for(state="visible")
        chat_btn.click()

    def click_meet_button(self):
        meet_btn = self.page.locator(self.teams.MEET_BUTTON)
        meet_btn.wait_for(state="visible")
        meet_btn.click()

    def click_people_button(self):
        people_btn = self.page.locator(self.teams.PEOPLE_BUTTON)
        people_btn.wait_for(state="visible")
        people_btn.click()

    def click_copilot_button(self):
        copilot_btn = self.page.locator(self.teams.COPILOT_BUTTON)
        copilot_btn.wait_for(state="visible")
        copilot_btn.click()

    def click_communities_button(self):
        communities_btn = self.page.locator(self.teams.COMMUNITIES_BUTTON)
        communities_btn.wait_for(state="visible")
        communities_btn.click()

    def click_activity_button(self):
        activity_btn = self.page.locator(self.teams.ACTIVITY_BUTTON)
        activity_btn.wait_for(state="visible")
        activity_btn.click()

    def click_calendar_button(self):
        calendar_btn = self.page.locator(self.teams.CALENDAR_BUTTON)
        calendar_btn.wait_for(state="visible")
        calendar_btn.click()

        new_meeting = self.page.locator(self.teams.NEW_MEETING_BUTTON)
        new_meeting.wait_for(state="visible")
        new_meeting.click()

        save_btn = self.page.locator(self.teams.SAVE_BUTTON)
        save_btn.wait_for(state="visible")
        save_btn.click()

    # Backwards compatibility alias for typo
    click_calender_button = click_calendar_button

    def close_browser(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()
