import getpass
import os
from pathlib import Path

import pytest
from pages.teams_sign import TeamsSign


def _load_env_file():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key and key not in os.environ:
                        os.environ[key] = val


_load_env_file()


def pytest_addoption(parser):
    parser.addoption("--email", action="store", default=None, help="Teams Email")
    parser.addoption("--password", action="store", default=None, help="Teams Password")


@pytest.fixture(scope="session")
def creds(request):
    email = request.config.getoption("--email") or os.environ.get("TEAMS_EMAIL")
    password = request.config.getoption("--password") or os.environ.get("TEAMS_PASSWORD")

    if not email:
        try:
            email = input("Enter Teams Email: ").strip()
        except OSError:
            raise RuntimeError(
                "Cannot prompt for email when stdin is captured. "
                "Please run pytest with '-s' (e.g. pytest tests/ -v -s), "
                "or pass --email / --password, or configure a .env file."
            )

    if not password:
        try:
            password = getpass.getpass("Enter Teams Password: ").strip()
        except OSError:
            raise RuntimeError(
                "Cannot prompt for password when stdin is captured. "
                "Please run pytest with '-s' (e.g. pytest tests/ -v -s), "
                "or pass --email / --password, or configure a .env file."
            )

    if not (email and password):
        raise RuntimeError("Email and password cannot be empty.")

    return email, password


@pytest.fixture(scope="session")
def teams(creds):
    email, password = creds

    t = TeamsSign()
    t.open_browser()
    t.sign_in_teams()
    t.send_email_id(email)
    t.enter_email_password(password)
    t.click_chat_button()
    t.click_meet_button()
    t.click_people_button()
    t.click_copilot_button()
    t.click_communities_button()
    t.click_activity_button()
    t.click_calender_button()

    yield t

    t.close_browser()