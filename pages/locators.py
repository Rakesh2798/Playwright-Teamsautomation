
class TeamsSignLocators:
    LOGIN_URL = "https://www.microsoft.com/en-in/microsoft-teams/log-in"

    SIGN_IN_BTN = "xpath=//span[normalize-space()='Sign in']"
    EMAIL_INPUT = "input[type='email'], #i0116"
    NEXT_BTN_1 = "#idSIButton9"
    NEXT_BTN_2 = "button[data-testid='primaryButton']"
    PASSWORD_INPUT = "#passwordEntry"
    #USE_YOUR_PASSWORD = "xpath=//span[@role='button' and normalize-space()='Use your password']"
    USE_YOUR_PASSWORD = "text=Use your password"
    NO_BUTTON = "xpath=//button[@type='submit' and normalize-space()='No']"
    NO = "button[data-testid='secondaryButton']"

    CHAT_BUTTON = "button[aria-label='Chat']"
    MEET_BUTTON = "button[aria-label='Meet']"
    PEOPLE_BUTTON = "button[aria-label='People']"
    COPILOT_BUTTON = "button[aria-label='Copilot']"
    COMMUNITIES_BUTTON = "button[aria-label='Communities']"
    CALENDAR_BUTTON = "button[aria-label='Calendar']"
    ACTIVITY_BUTTON = "button[aria-label='Activity']"

    NEW_MEETING_BUTTON = "button[title='Schedule a new meeting']"
    SAVE_BUTTON = "button[data-tid='calv2-sf-save']"
