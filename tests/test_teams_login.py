from playwright.sync_api import expect


def test_activity_button_presence(teams):
    activity_btn = teams.page.locator(teams.teams.ACTIVITY_BUTTON)
    expect(activity_btn).to_be_visible(timeout=60000)


def test_chat_button_presence(teams):
    chat_btn = teams.page.locator(teams.teams.CHAT_BUTTON)
    expect(chat_btn).to_be_visible(timeout=60000)


def test_meet_button_presence(teams):
    meet_btn = teams.page.locator(teams.teams.MEET_BUTTON)
    expect(meet_btn).to_be_visible(timeout=60000)


def test_calendar_button_presence(teams):
    calendar_btn = teams.page.locator(teams.teams.CALENDAR_BUTTON)
    expect(calendar_btn).to_be_visible(timeout=60000)


def test_people_button_presence(teams):
    people_btn = teams.page.locator(teams.teams.PEOPLE_BUTTON)
    expect(people_btn).to_be_visible(timeout=60000)


def test_copilot_button_presence(teams):
    copilot_btn = teams.page.locator(teams.teams.COPILOT_BUTTON)
    expect(copilot_btn).to_be_visible(timeout=60000)


def test_communities_button_presence(teams):
    communities_btn = teams.page.locator(teams.teams.COMMUNITIES_BUTTON)
    expect(communities_btn).to_be_visible(timeout=60000)
