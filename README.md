# OrangeHRM Playwright QA (Python)

# OrangeHRM Playwright QA (Python)

![Test Pipeline](https://github.com/HusainCode/OrangeHRM-Quality-Engineering/actions/workflows/ci.yml/badge.svg?branch=main&event=push)

Professional QA automation demonstration using **Playwright + Pytest** against the public **OrangeHRM Demo** site.  
Focus: clean Page Object Model, reliable tests, CI, and reporting—built to mirror a real QA workflow.

## Demo Under Test

- **Site:** https://opensource-demo.orangehrmlive.com
- **Creds:** `Admin / admin123` (public)

## What This Covers

- ✅ Login (valid/invalid)
- ✅ PIM: Add → Verify in list → Delete
- ✅ Form validation (required fields)
- ✅ Logout
- ✅ Table interactions (sorting/filtering) — optional enhancement

## Why This Repo Matters

- Realistic enterprise web app flows
- Cross-browser CI with artifacts (HTML report, traces, screenshots, videos)
- Clear test design with IDs and reliability tactics

## Tech Stack

- **Core:** Playwright (Python), Pytest
- **Plugins:** `pytest-playwright`, `pytest-html`, `pytest-xdist`, `pytest-rerunfailures`, `python-dotenv`, optional `allure-pytest`
- **CI:** GitHub Actions (Ubuntu), matrix: Chromium/Firefox/WebKit
- **Artifacts:** HTML report, Playwright trace/screenshot/video, optional Allure

## Test Design & IDs

- **LOGIN-001** — Valid login → Dashboard visible
- **LOGIN-002** — Invalid login → “Invalid credentials” shown
- **PIM-ADD-001** — Create employee (min fields) → success toast
- **PIM-VAL-001** — Save blocked when required field missing
- **PIM-LIST-001** — New employee appears via search/filter
- **PIM-DEL-001** — Delete employee → success toast + not listed
- **NAV-LOGOUT-001** — Logout returns to login

## Reliability Practices

- Stable locators (roles/text), minimal page objects
- Unique data per test (randomized names)
- 1 rerun on known flakes; isolate with a new browser context per test
- Auto-waits; explicit waits only at state transitions

## Local Setup (summary)

> No app code here; this repo documents how to run tests once you add them.

1. Python 3.11+, Git, Chrome/Firefox/WebKit support
2. Create a virtualenv and install: Playwright, Pytest, plugins
3. Run `playwright install` to fetch browsers
4. Configure env (optional): `BASE_URL`, `ORANGEHRM_USER`, `ORANGEHRM_PASS`

## Running (once tests are added)

- Smoke: login only (fast)
- Core suite: login + PIM add/search/delete + validation + logout
- Cross-browser: Chromium/Firefox/WebKit

Suggested commands (after you add tests):

- `pytest -n auto --browser chromium`
- `pytest --browser firefox`
- `pytest --reruns 1 --reruns-delay 2`

## Reports & Artifacts

- **HTML report:** generated per run (store in `reports/`)
- **Playwright artifacts:** traces, screenshots, videos on failure (`test-results/`)
- **Allure (optional):** `--alluredir=allure-results` → publish via CI or serve locally

## CI/CD (GitHub Actions)

- PR: smoke (Chromium)
- Push to `main`: core matrix (Chromium/Firefox/WebKit)
- Nightly: full cross-browser + optional Allure publish  
  Artifacts uploaded: HTML report, traces, screenshots, videos.

### 🧩 Folder Overview

- **`pages/`** — Reusable Page Object classes encapsulating UI locators and actions.
- **`tests/`** — End-to-end Pytest suites for functional and regression coverage.
- **`config/`** — Environment variables, credentials, and configuration files.
- **`utils/`** — Shared helpers for random data, assertions, and utilities.
- **`reports/`** — HTML, JSON, and Allure test reports for traceability.
- **`.github/workflows/`** — GitHub Actions CI/CD pipelines for automated testing.

---.
