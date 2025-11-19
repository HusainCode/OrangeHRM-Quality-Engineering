# OrangeHRM Test Automation Framework

![Test Pipeline](https://github.com/HusainCode/OrangeHRM-Quality-Engineering/actions/workflows/ci.yml/badge.svg?branch=main&event=push)

A professional, enterprise-grade test automation framework for OrangeHRM using Playwright and Python. Built with clean architecture, smart design patterns, and real-world QA best practices in mind.

## What's This About?

I built this framework to test the public OrangeHRM demo (https://opensource-demo.orangehrmlive.com) using Playwright + Pytest. The goal wasn't just to write tests—it was to create something that feels like what you'd actually use on a real project: maintainable, scalable, and easy for other engineers to jump into.

**Quick highlights:**
- Login flows (valid/invalid credentials, field validation)
- Employee management (add, search, delete employees)
- Admin user management
- Dashboard quick actions
- Performance and API testing examples
- Cross-browser testing (Chromium, Firefox, WebKit)
- Clean Page Object Model architecture
- Randomized test data for isolation
- CI/CD pipeline with GitHub Actions

---

## Why This Framework?

**Clean separation of concerns:**
- Page Objects handle *what's on the page* (locators + actions only)
- Tests handle *what you're actually testing* (business logic + assertions)
- Config manages environment settings
- Utils provide reusable helpers

**Real-world practices:**
- No hardcoded credentials (environment variables)
- Random data generation (tests don't step on each other)
- Proper waits (no `sleep(3)` nonsense)
- Centralized fixtures (DRY principle)
- Parallel execution support
- Auto-retry flaky tests
- Screenshot/trace capture on failure

---

## Tech Stack

**Core:**
- Python 3.11+
- Playwright (browser automation)
- Pytest (test framework)

**Key plugins:**
- `pytest-playwright` - Playwright integration
- `pytest-xdist` - Parallel test execution
- `pytest-rerunfailures` - Retry flaky tests
- `pytest-html` - HTML test reports
- `python-dotenv` - Environment configuration

**CI/CD:**
- GitHub Actions with multi-browser matrix
- Separate smoke/regression/performance test jobs
- Artifact uploads (screenshots, traces, videos)

---

## Project Structure

Here's how everything is organized:

```
OrangeHRM-Quality-Engineering/
├── config/                          # Configuration management
│   ├── __init__.py
│   └── settings.py                  # Environment settings, credentials, URLs
│
├── pages/                           # Page Object Models
│   ├── __init__.py
│   ├── base_page.py                 # Base class for all pages
│   ├── login_page.py                # Login page
│   ├── dashboard_page.py            # Dashboard
│   ├── pim_page.py                  # Employee management
│   ├── admin_page.py                # User management
│   ├── leave_page.py                # Leave management
│   ├── time_page.py                 # Timesheet management
│   └── myinfo_page.py               # Employee self-service
│
├── tests/                           # Test suites
│   ├── conftest.py                  # Centralized fixtures
│   ├── auth/                        # Authentication tests
│   │   ├── test_login.py
│   │   └── test_navigation.py
│   ├── pim/                         # Employee management tests
│   │   └── test_pim.py
│   ├── admin/                       # Admin tests
│   │   └── test_admin.py
│   ├── dashboard/                   # Dashboard tests
│   │   └── test_dashboard.py
│   ├── performance/                 # Performance tests
│   │   └── test_performance.py
│   └── api/                         # API tests
│       └── test_api.py
│
├── utils/                           # Utility modules
│   ├── __init__.py
│   ├── data_generator.py            # Random test data
│   ├── custom_waits.py              # Smart waiting strategies
│   └── custom_assertions.py         # Reusable assertions
│
├── reports/                         # Test reports and artifacts
│   ├── screenshots/
│   ├── traces/
│   └── videos/
│
├── .github/workflows/               # CI/CD pipelines
│   └── ci.yml                       # GitHub Actions workflow
│
├── .env.example                     # Environment template
├── pytest.ini                       # Pytest configuration
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- A terminal you're comfortable with

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/HusainCode/OrangeHRM-Quality-Engineering.git
   cd OrangeHRM-Quality-Engineering
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

5. **Set up environment variables** (optional)
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

That's it! You're ready to run tests.

---

## Running Tests

### Quick Start

```bash
# Run all tests
pytest

# Run smoke tests only (fast)
pytest -m smoke

# Run regression tests
pytest -m regression

# Run specific module
pytest tests/auth/
pytest tests/pim/

# Run with specific browser
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Parallel Execution

```bash
# Run tests in parallel (auto-detect CPU cores)
pytest -n auto

# Run with specific number of workers
pytest -n 4
```

### With Retries (for flaky tests)

```bash
# Retry failures once with 2-second delay
pytest --reruns 1 --reruns-delay 2
```

### Performance Tests

```bash
pytest -m performance
```

### API Tests

```bash
pytest -m api
```

---

## Test Markers

Tests are organized with pytest markers:

- `@pytest.mark.smoke` - Quick smoke tests (login, basic navigation)
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.auth` - Authentication tests
- `@pytest.mark.pim` - Employee management tests
- `@pytest.mark.admin` - Admin/user management tests
- `@pytest.mark.dashboard` - Dashboard tests
- `@pytest.mark.performance` - Performance tests
- `@pytest.mark.api` - API tests
- `@pytest.mark.slow` - Slow-running tests

Run specific markers:
```bash
pytest -m "smoke and not slow"
pytest -m "regression and pim"
```

---

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and customize:

```bash
ENV=demo                    # Environment (demo, staging, dev)
HEADLESS=true              # Run browser in headless mode
BROWSER=chromium           # Default browser
ORANGEHRM_USER=Admin       # Login username
ORANGEHRM_PASSWORD=admin123  # Login password
```

### Pytest Configuration

Check `pytest.ini` for test discovery, markers, logging, and report settings.

---

## Test Reports

### HTML Report

After running tests, find the HTML report at:
```
reports/report.html
```

### Screenshots on Failure

Auto-captured in `reports/screenshots/` when tests fail.

### Playwright Traces

Detailed execution traces saved in `reports/traces/` for debugging.

### Videos (optional)

Enable in config to record test execution videos.

---

## CI/CD Pipeline

The framework includes a GitHub Actions workflow with three jobs:

### 1. **Smoke Tests** (on Pull Requests)
- Runs quickly on every PR
- Uses only Chromium browser
- Fast feedback loop

### 2. **Regression Tests** (on Push to Main)
- Full test suite across all browsers (Chromium, Firefox, WebKit)
- Runs in parallel for speed
- Auto-retries flaky tests
- Uploads artifacts (reports, screenshots, traces)

### 3. **Performance Tests** (Nightly + Manual)
- Scheduled to run nightly at 2 AM UTC
- Can be triggered manually
- Tracks page load times and API performance

---

## Test Coverage

### ✅ Implemented

**Authentication & Navigation:**
- LOGIN-001: Valid login redirects to dashboard
- LOGIN-002: Invalid credentials show error
- LOGIN-003/004/005: Field validation (required fields)
- NAV-LOGOUT-001: Logout returns to login

**PIM (Employee Management):**
- PIM-ADD-001: Create employee with minimum fields
- PIM-VAL-001: Validation when required field missing
- PIM-LIST-001: New employee appears in search
- PIM-DEL-001: Delete employee and verify removal

**Admin (User Management):**
- ADMIN-ADD-001: Create system user
- ADMIN-DEL-001: Delete user
- ADMIN-VAL-001: Field validation

**Dashboard:**
- DASH-001: Dashboard widgets load
- DASH-QA-001/002/003: Quick action navigation

**Performance:**
- PERF-001: Login page load time
- PERF-002: Dashboard load after login
- PERF-003: Employee search response time
- PERF-004: Page navigation performance

**API:**
- API-AUTH-001: Login API status codes
- API-AUTH-002: Unauthorized request handling
- API-PERF-001: API response times

### 📝 Future Enhancements

- Leave request/approval workflows
- Timesheet submission
- My Info document uploads
- Recruitment module
- Reports generation
- More comprehensive API testing

---

## Tips & Tricks

**Debugging failed tests:**
```bash
# Run with headed browser to watch
pytest --headed

# Slow down execution
pytest --slowmo 1000

# Run specific test
pytest tests/auth/test_login.py::TestLogin::test_valid_login_redirects_to_dashboard
```

**Generate fresh test data:**
The framework automatically generates random employee names, usernames, and IDs for each test run. Check `utils/data_generator.py` for details.

**Custom waits:**
Instead of using `time.sleep()`, use smart waits from `utils/custom_waits.py`:
```python
from utils import waits

waits.wait_for_success_toast(page)
waits.wait_for_network_idle(page)
waits.wait_for_element_visible(locator)
```

**Page Object pattern:**
Keep tests clean by using page objects:
```python
# Bad: locators in test
page.locator('input[name="username"]').fill("Admin")

# Good: page object method
login_page.enter_username("Admin")
```

---

## Common Issues

**Timeout errors?**
- Check your internet connection
- OrangeHRM demo site might be slow
- Increase timeouts in `.env` if needed

**Tests failing randomly?**
- Enable retries: `pytest --reruns 1`
- Check if tests are properly isolated
- Verify test data isn't conflicting

**Browser not found?**
- Run `playwright install` again
- For specific browser: `playwright install chromium`

---

## Contributing

Got ideas for improvements? Found a bug? Feel free to:
1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## License

This is a portfolio/demonstration project. Feel free to use it as a reference or starting point for your own automation framework.

---

## Contact

Built by [HusainCode](https://github.com/HusainCode)

Questions? Open an issue or reach out!

---

**Pro tip:** If you're interviewing for a QA automation role, this framework shows you understand:
- Clean architecture (separation of concerns)
- Design patterns (Page Object Model)
- Modern tooling (Playwright, Pytest)
- CI/CD integration
- Real-world best practices

Use it as a conversation starter! 🚀
