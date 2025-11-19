"""Page Object Models for OrangeHRM"""
from .base_page import BasePage
from .login_page import LoginPage
from .dashboard_page import DashboardPage
from .pim_page import PimPage
from .admin_page import AdminPage
from .leave_page import LeavePage
from .time_page import TimePage
from .myinfo_page import MyInfoPage

__all__ = [
    "BasePage",
    "LoginPage",
    "DashboardPage",
    "PimPage",
    "AdminPage",
    "LeavePage",
    "TimePage",
    "MyInfoPage",
]
