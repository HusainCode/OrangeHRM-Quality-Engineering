"""
My Info Page Object - handles employee self-service.
Includes personal details, contact info, documents, profile picture.
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class MyInfoPage(BasePage):
    """My Info page object for OrangeHRM"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "web/index.php/pim/viewPersonalDetails/empNumber/7"

    # ---------- Locators ----------
    @property
    def my_info_menu_link(self):
        """My Info menu link"""
        return self.page.get_by_role("link", name="My Info")

    @property
    def personal_details_tab(self):
        """Personal Details tab"""
        return self.page.get_by_role("link", name="Personal Details")

    @property
    def contact_details_tab(self):
        """Contact Details tab"""
        return self.page.get_by_role("link", name="Contact Details")

    @property
    def emergency_contacts_tab(self):
        """Emergency Contacts tab"""
        return self.page.get_by_role("link", name="Emergency Contacts")

    @property
    def dependents_tab(self):
        """Dependents tab"""
        return self.page.get_by_role("link", name="Dependents")

    @property
    def immigration_tab(self):
        """Immigration tab"""
        return self.page.get_by_role("link", name="Immigration")

    @property
    def qualifications_tab(self):
        """Qualifications tab"""
        return self.page.get_by_role("link", name="Qualifications")

    # Profile Picture
    @property
    def profile_picture(self):
        """Profile picture element"""
        return self.page.locator('.employee-image')

    @property
    def profile_picture_input(self):
        """Profile picture file input"""
        return self.page.locator('input[type="file"]').first

    @property
    def upload_picture_button(self):
        """Upload profile picture button (may be hidden)"""
        return self.page.locator('.employee-image-action')

    # Personal Details
    @property
    def first_name_input(self):
        """First name input"""
        return self.page.locator('input[name="firstName"]')

    @property
    def middle_name_input(self):
        """Middle name input"""
        return self.page.locator('input[name="middleName"]')

    @property
    def last_name_input(self):
        """Last name input"""
        return self.page.locator('input[name="lastName"]')

    @property
    def employee_id_input(self):
        """Employee ID input"""
        return self.page.locator('.oxd-input').nth(4)

    @property
    def license_number_input(self):
        """Driver's license number input"""
        return self.page.locator('.oxd-input').nth(5)

    @property
    def license_expiry_date_input(self):
        """License expiry date input"""
        return self.page.locator('.oxd-input').nth(6)

    @property
    def nationality_dropdown(self):
        """Nationality dropdown"""
        return self.page.locator('.oxd-select-text-input').first

    @property
    def marital_status_dropdown(self):
        """Marital status dropdown"""
        return self.page.locator('.oxd-select-text-input').nth(1)

    @property
    def date_of_birth_input(self):
        """Date of birth input"""
        return self.page.locator('.oxd-input').nth(7)

    @property
    def gender_male_radio(self):
        """Male gender radio button"""
        return self.page.locator('input[value="1"]').first

    @property
    def gender_female_radio(self):
        """Female gender radio button"""
        return self.page.locator('input[value="2"]').first

    @property
    def save_button(self):
        """Save button"""
        return self.page.get_by_role("button", name="Save").first

    # Attachments/Documents
    @property
    def add_attachment_button(self):
        """Add attachment button"""
        return self.page.get_by_role("button", name="Add")

    @property
    def attachment_file_input(self):
        """Attachment file input"""
        return self.page.locator('input[type="file"]')

    @property
    def attachment_comment_textarea(self):
        """Attachment comment textarea"""
        return self.page.locator('textarea').first

    @property
    def attachments_table(self):
        """Attachments table"""
        return self.page.locator('.oxd-table-body')

    @property
    def attachments_rows(self):
        """Attachment table rows"""
        return self.page.locator('.oxd-table-card')

    # ---------- Actions ----------
    def navigate(self):
        """Navigate to My Info page"""
        self.click_menu_item("My Info")

    def click_personal_details_tab(self):
        """Click Personal Details tab"""
        self.personal_details_tab.click()

    def click_contact_details_tab(self):
        """Click Contact Details tab"""
        self.contact_details_tab.click()

    def upload_profile_picture(self, file_path: str):
        """Upload profile picture"""
        self.profile_picture_input.set_input_files(file_path)

    def enter_first_name(self, first_name: str):
        """Enter first name"""
        self.first_name_input.fill(first_name)

    def enter_middle_name(self, middle_name: str):
        """Enter middle name"""
        self.middle_name_input.fill(middle_name)

    def enter_last_name(self, last_name: str):
        """Enter last name"""
        self.last_name_input.fill(last_name)

    def enter_license_number(self, license_number: str):
        """Enter driver's license number"""
        self.license_number_input.fill(license_number)

    def select_nationality(self, nationality: str):
        """Select nationality from dropdown"""
        self.nationality_dropdown.click()
        self.page.get_by_role("option", name=nationality).click()

    def select_marital_status(self, status: str):
        """Select marital status from dropdown"""
        self.marital_status_dropdown.click()
        self.page.get_by_role("option", name=status).click()

    def enter_date_of_birth(self, date: str):
        """Enter date of birth (YYYY-MM-DD)"""
        self.date_of_birth_input.fill(date)

    def select_gender_male(self):
        """Select male gender"""
        self.gender_male_radio.click()

    def select_gender_female(self):
        """Select female gender"""
        self.gender_female_radio.click()

    def click_save(self):
        """Click save button"""
        self.save_button.click()

    def add_attachment(self, file_path: str, comment: str = ""):
        """Add a document attachment"""
        self.add_attachment_button.click()
        self.attachment_file_input.set_input_files(file_path)
        if comment:
            self.attachment_comment_textarea.fill(comment)
        self.save_button.click()

    def get_attachment_count(self) -> int:
        """Get number of attachments"""
        return self.attachments_rows.count()

    def is_profile_picture_visible(self) -> bool:
        """Check if profile picture is visible"""
        return self.profile_picture.is_visible()
