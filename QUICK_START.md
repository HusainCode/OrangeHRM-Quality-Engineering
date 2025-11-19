# ⚡ Quick Start Guide

Get up and running in 5 minutes!

## 1. Install Everything

```bash
# Install dependencies
pip install -r requirements.txt

# Install browsers
playwright install
```

## 2. Run Your First Test

```bash
# Run smoke tests (fastest)
pytest -m smoke -v

# Run all tests
pytest -v

# Run specific test file
pytest tests/auth/test_login.py -v
```

## 3. Common Commands

```bash
# Run in parallel (fast)
pytest -n auto

# Run with retries (for flaky tests)
pytest --reruns 1 --reruns-delay 2

# Run specific browser
pytest --browser firefox

# Run with visible browser (for debugging)
pytest --headed --slowmo 1000

# Run specific test
pytest tests/auth/test_login.py::TestLogin::test_valid_login_redirects_to_dashboard
```

## 4. Viewing Reports

After running tests:
- **HTML Report:** `reports/report.html`
- **Screenshots:** `reports/screenshots/` (on failure)
- **Traces:** `reports/traces/` (for debugging)

## 5. Optional: Configure Environment

```bash
# Copy env template
cp .env.example .env

# Edit with your preferred settings
# (Optional - defaults work fine)
```

## 6. Project Structure at a Glance

```
config/       → Settings, credentials, URLs
pages/        → Page Objects (what's on the page)
tests/        → Test scenarios (what you're testing)
utils/        → Helpers (waits, assertions, data)
reports/      → Test results
```

## 7. Writing Your First Test

```python
import pytest
from pages import LoginPage
from config import config
from utils import assertions

@pytest.mark.smoke
def test_my_first_test(login_page: LoginPage, page):
    """My first test"""
    login_page.navigate()
    login_page.login(config.get_username(), config.get_password())
    assertions.assert_on_dashboard(page)
```

## 8. Next Steps

1. ✅ Read `README.md` for full documentation
2. ✅ Check `REFACTORING_SUMMARY.md` for detailed changes
3. ✅ Explore example tests in `tests/auth/` and `tests/pim/`
4. ✅ Review Page Objects in `pages/`

## Need Help?

- Check `README.md` for detailed docs
- Review `REFACTORING_SUMMARY.md` for architecture
- Look at example tests for patterns

---

**That's it!** You're ready to test. 🚀
