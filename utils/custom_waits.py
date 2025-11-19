"""
Custom wait utilities to replace hard-coded timeouts.
Provides intelligent waiting strategies for various UI states.
"""
from playwright.sync_api import Page, Locator, expect
from typing import Callable, Optional, Any


class CustomWaits:
    """Custom wait utilities for Playwright"""

    @staticmethod
    def wait_for_toast_message(page: Page, timeout: int = 10000) -> Locator:
        """Wait for toast notification to appear"""
        toast = page.locator('.oxd-toast')
        expect(toast).to_be_visible(timeout=timeout)
        return toast

    @staticmethod
    def wait_for_success_toast(page: Page, timeout: int = 10000) -> Locator:
        """Wait for success toast to appear"""
        toast = page.locator('.oxd-toast--success')
        expect(toast).to_be_visible(timeout=timeout)
        return toast

    @staticmethod
    def wait_for_error_toast(page: Page, timeout: int = 10000) -> Locator:
        """Wait for error toast to appear"""
        toast = page.locator('.oxd-toast--error')
        expect(toast).to_be_visible(timeout=timeout)
        return toast

    @staticmethod
    def wait_for_page_load(page: Page, state: str = "domcontentloaded"):
        """Wait for page to reach specific load state"""
        page.wait_for_load_state(state)

    @staticmethod
    def wait_for_network_idle(page: Page, timeout: int = 30000):
        """Wait for network to be idle (no more than 2 connections for 500ms)"""
        page.wait_for_load_state("networkidle", timeout=timeout)

    @staticmethod
    def wait_for_url_change(page: Page, expected_pattern: str, timeout: int = 15000):
        """Wait for URL to match a pattern"""
        import re
        expect(page).to_have_url(re.compile(expected_pattern), timeout=timeout)

    @staticmethod
    def wait_for_element_visible(locator: Locator, timeout: int = 10000):
        """Wait for element to be visible"""
        expect(locator).to_be_visible(timeout=timeout)

    @staticmethod
    def wait_for_element_hidden(locator: Locator, timeout: int = 10000):
        """Wait for element to be hidden"""
        expect(locator).to_be_hidden(timeout=timeout)

    @staticmethod
    def wait_for_text_content(locator: Locator, text: str, timeout: int = 10000):
        """Wait for element to contain specific text"""
        expect(locator).to_contain_text(text, timeout=timeout)

    @staticmethod
    def wait_for_attribute(locator: Locator, attribute: str, value: str, timeout: int = 10000):
        """Wait for element to have specific attribute value"""
        expect(locator).to_have_attribute(attribute, value, timeout=timeout)

    @staticmethod
    def wait_for_count(locator: Locator, count: int, timeout: int = 10000):
        """Wait for specific number of elements"""
        expect(locator).to_have_count(count, timeout=timeout)

    @staticmethod
    def wait_for_enabled(locator: Locator, timeout: int = 10000):
        """Wait for element to be enabled"""
        expect(locator).to_be_enabled(timeout=timeout)

    @staticmethod
    def wait_for_disabled(locator: Locator, timeout: int = 10000):
        """Wait for element to be disabled"""
        expect(locator).to_be_disabled(timeout=timeout)

    @staticmethod
    def wait_for_table_load(page: Page, table_selector: str = '.oxd-table-body', timeout: int = 15000):
        """Wait for data table to load"""
        table = page.locator(table_selector)
        expect(table).to_be_visible(timeout=timeout)
        page.wait_for_load_state("networkidle", timeout=timeout)

    @staticmethod
    def wait_for_condition(
        condition: Callable[[], bool],
        timeout: int = 10000,
        interval: int = 100,
        error_message: str = "Condition not met within timeout"
    ) -> bool:
        """
        Wait for a custom condition to be true.

        Args:
            condition: A callable that returns True when condition is met
            timeout: Maximum time to wait in milliseconds
            interval: Check interval in milliseconds
            error_message: Message to show if condition not met

        Returns:
            True if condition met, raises TimeoutError otherwise
        """
        import time
        start_time = time.time() * 1000

        while (time.time() * 1000 - start_time) < timeout:
            if condition():
                return True
            time.sleep(interval / 1000)

        raise TimeoutError(error_message)

    @staticmethod
    def smart_wait(page: Page, short_wait: int = 500):
        """
        Smart wait - use sparingly, only when absolutely necessary.
        Prefer explicit waits for specific conditions.
        """
        page.wait_for_timeout(short_wait)


# Convenience instance
waits = CustomWaits()
