"""
Central configuration for the test framework.
Handles environment variables, base URLs, credentials, and test settings.
"""
import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@dataclass
class Config:
    """Main configuration class for test framework"""

    # Environment
    ENV: str = os.getenv("ENV", "demo")

    # Base URLs for different environments
    BASE_URLS = {
        "demo": "https://opensource-demo.orangehrmlive.com",
        "staging": "https://staging-demo.orangehrmlive.com",  # example
        "dev": "http://localhost:8080",  # example
    }

    # Credentials (per environment)
    CREDENTIALS = {
        "demo": {
            "username": os.getenv("ORANGEHRM_USER", "Admin"),
            "password": os.getenv("ORANGEHRM_PASSWORD", "admin123"),
        },
        "staging": {
            "username": os.getenv("STAGING_USER", "Admin"),
            "password": os.getenv("STAGING_PASSWORD", "admin123"),
        },
        "dev": {
            "username": os.getenv("DEV_USER", "admin"),
            "password": os.getenv("DEV_PASSWORD", "admin"),
        },
    }

    # Browser settings
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER: str = os.getenv("BROWSER", "chromium")
    SLOW_MO: int = int(os.getenv("SLOW_MO", "0"))

    # Timeout settings (in milliseconds)
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "30000"))
    NAVIGATION_TIMEOUT: int = int(os.getenv("NAVIGATION_TIMEOUT", "30000"))
    ACTION_TIMEOUT: int = int(os.getenv("ACTION_TIMEOUT", "10000"))

    # Test settings
    SCREENSHOT_ON_FAILURE: bool = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"
    VIDEO_ON_FAILURE: bool = os.getenv("VIDEO_ON_FAILURE", "false").lower() == "true"
    TRACE_ON_FAILURE: bool = os.getenv("TRACE_ON_FAILURE", "true").lower() == "true"

    # Retry settings
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "1"))
    RETRY_DELAY: int = int(os.getenv("RETRY_DELAY", "2"))

    # Parallel execution
    WORKERS: str = os.getenv("WORKERS", "auto")

    # Report paths
    REPORTS_DIR: str = os.getenv("REPORTS_DIR", "reports")
    SCREENSHOTS_DIR: str = os.getenv("SCREENSHOTS_DIR", "reports/screenshots")
    VIDEOS_DIR: str = os.getenv("VIDEOS_DIR", "reports/videos")
    TRACES_DIR: str = os.getenv("TRACES_DIR", "reports/traces")

    @classmethod
    def get_base_url(cls) -> str:
        """Get base URL for current environment"""
        return cls.BASE_URLS.get(cls.ENV, cls.BASE_URLS["demo"])

    @classmethod
    def get_credentials(cls) -> dict:
        """Get credentials for current environment"""
        return cls.CREDENTIALS.get(cls.ENV, cls.CREDENTIALS["demo"])

    @classmethod
    def get_username(cls) -> str:
        """Get username for current environment"""
        return cls.get_credentials()["username"]

    @classmethod
    def get_password(cls) -> str:
        """Get password for current environment"""
        return cls.get_credentials()["password"]


# Create a singleton instance
config = Config()
