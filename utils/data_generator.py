"""
Random test data generators to ensure test isolation and uniqueness.
"""
import random
import string
from datetime import datetime, timedelta
from typing import Optional


class DataGenerator:
    """Generate random test data for various test scenarios"""

    @staticmethod
    def random_string(length: int = 8, prefix: str = "") -> str:
        """Generate a random string with optional prefix"""
        letters = string.ascii_lowercase
        random_part = "".join(random.choice(letters) for _ in range(length))
        return f"{prefix}{random_part}" if prefix else random_part

    @staticmethod
    def random_number(min_val: int = 1000, max_val: int = 9999) -> int:
        """Generate a random number within range"""
        return random.randint(min_val, max_val)

    @staticmethod
    def random_email(domain: str = "example.com") -> str:
        """Generate a random email address"""
        username = DataGenerator.random_string(8)
        return f"{username}@{domain}"

    @staticmethod
    def random_phone(country_code: str = "+1") -> str:
        """Generate a random phone number"""
        number = "".join([str(random.randint(0, 9)) for _ in range(10)])
        return f"{country_code}{number}"

    @staticmethod
    def random_first_name() -> str:
        """Generate a random first name"""
        first_names = [
            "James", "Mary", "John", "Patricia", "Robert", "Jennifer",
            "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
            "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah",
            "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Lisa",
            "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra"
        ]
        return random.choice(first_names)

    @staticmethod
    def random_last_name() -> str:
        """Generate a random last name"""
        last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
            "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez",
            "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
            "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
            "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis"
        ]
        return random.choice(last_names)

    @staticmethod
    def random_full_name() -> tuple[str, str]:
        """Generate a random full name (first, last)"""
        return DataGenerator.random_first_name(), DataGenerator.random_last_name()

    @staticmethod
    def random_employee_id() -> str:
        """Generate a random employee ID"""
        return f"EMP{DataGenerator.random_number(10000, 99999)}"

    @staticmethod
    def random_username(prefix: str = "user") -> str:
        """Generate a random username"""
        return f"{prefix}_{DataGenerator.random_string(6)}"

    @staticmethod
    def random_password(length: int = 12) -> str:
        """Generate a random password with mixed characters"""
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        return "".join(random.choice(characters) for _ in range(length))

    @staticmethod
    def random_date(days_from_now: int = 0, date_format: str = "%Y-%m-%d") -> str:
        """Generate a random date relative to today"""
        target_date = datetime.now() + timedelta(days=days_from_now)
        return target_date.strftime(date_format)

    @staticmethod
    def random_date_range(start_days: int = 1, end_days: int = 5) -> tuple[str, str]:
        """Generate a random date range (start, end)"""
        start_date = DataGenerator.random_date(start_days)
        end_date = DataGenerator.random_date(end_days)
        return start_date, end_date

    @staticmethod
    def random_address() -> dict:
        """Generate a random address"""
        return {
            "street": f"{DataGenerator.random_number(1, 999)} {DataGenerator.random_string(8).title()} St",
            "city": random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]),
            "state": random.choice(["NY", "CA", "IL", "TX", "AZ"]),
            "zip": f"{DataGenerator.random_number(10000, 99999)}",
            "country": "United States"
        }

    @staticmethod
    def random_choice(choices: list):
        """Return a random choice from a list"""
        return random.choice(choices)

    @staticmethod
    def unique_timestamp() -> str:
        """Generate a unique timestamp-based identifier"""
        return datetime.now().strftime("%Y%m%d_%H%M%S_%f")


# Convenience instance
data = DataGenerator()
