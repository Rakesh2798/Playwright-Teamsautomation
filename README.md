# Microsoft Teams Playwright Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-1.40+-green?logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-9.0+-orange?logo=pytest)
![Design Pattern](https://img.shields.io/badge/Pattern-Page_Object_Model_(POM)-purple)

A robust, modular test automation framework designed for end-to-end web testing of **Microsoft Teams** using **Python**, **Playwright**, and **Pytest**. Built following enterprise SDET best practices, clean Page Object architecture, and zero hardcoded sleeps.

---

## 🌟 Key Features & Architectural Highlights

- **Page Object Model (POM)**: Complete separation of concerns:
  - `pages/locators.py`: Centralized repository of selectors.
  - `pages/teams_sign.py`: Encapsulated page behaviors and UI interactions.
  - `tests/`: High-level test assertions focused on business requirements.
- **Resilient Auto-Waiting**: Zero arbitrary `time.sleep()` calls. Uses Playwright's built-in web-first auto-waiting and dynamic locator state checks (`wait_for(state="visible")`) for maximum reliability and minimum execution time.
- **Session-Scoped Fixtures**: Login orchestration runs once per test session via `conftest.py`, avoiding repetitive sign-in overhead across tests.
- **Multi-Window / Popup Handling**: Handles authentication windows and redirects across multiple browser pages seamlessly.
- **Flexible & Secure Credential Handling**:
  - **Masked Interactive Input**: Prompts for password securely without echoing characters (`getpass`).
  - **CLI Options**: Supports `--email` and `--password` command-line flags.
  - **Environment Variables**: Supports `$env:TEAMS_EMAIL` and `$env:TEAMS_PASSWORD` or local `.env` files.

---

## 📁 Project Directory Structure

```text
Playwright/
├── pages/
│   ├── locators.py         # UI locators for authentication and navigation
│   └── teams_sign.py       # Page Object for Teams authentication & navigation
├── tests/
│   ├── conftest.py         # Pytest fixtures, CLI options, credential resolution
│   └── test_teams_login.py # Navigation and UI button presence verification tests
├── .gitignore              # Ignores venv, cache, and sensitive .env files
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation and architectural overview
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+** (Tested on Python 3.12)
- Node.js runtime (managed automatically by Playwright)

### 2. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/teams-playwright-tests.git
   cd teams-playwright-tests
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

---

## 🧪 Running the Tests

### Option A: Interactive Prompt (Secure Password Masking)
Run with the `-s` flag so standard input is not captured:
```powershell
pytest tests/ -v -s
```
You will be prompted:
```text
Enter Teams Email: your_email@outlook.com
Enter Teams Password: <hidden keystrokes>
```

### Option B: Command-Line Flags
Pass credentials directly during invocation:
```powershell
pytest tests/ -v -s --email "user@outlook.com" --password "your_password"
```

### Option C: Environment Variables or `.env` File
Create a `.env` file in the project root:
```env
TEAMS_EMAIL=user@outlook.com
TEAMS_PASSWORD=your_password
```
Or set them in your PowerShell session:
```powershell
$env:TEAMS_EMAIL = "user@outlook.com"
$env:TEAMS_PASSWORD = "your_password"
pytest tests/ -v -s
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
