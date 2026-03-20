import allure
import pytest
from utils.config import ConfigReader


@allure.epic("מערכת ניהול משתמשים")
@allure.feature("תהליך התחברות (Login)")
class TestLogin:

    @allure.story("התחברות מוצלחת עם פרטים תקינים")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("התחברות לאתר עם יוזר תקין מקובץ קונפיג")
    @allure.title("בדיקת התחברות לאתר")
    def test_valid_login(self, setup_ui):
        with allure.step("קריאת נתונים מהקונפיג"):
            user = ConfigReader.read_config('user_details', 'user')
            password = ConfigReader.read_config('user_details', 'password')

        setup_ui.login_page.fill_page(user, password)
        with allure.step("ווידוא הגעה לדף המוצרים"):
            assert setup_ui.inventory_page.get_title() == "Products", "Should have reached the inventory page"

    @allure.story("חסימת משתמש עם פרטים שגויים")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("בדיקה שלילית - הזנת פרטים שגויים ואימות הודעת שגיאה")
    @allure.title("בדיקה שלילית: אימות הודעת שגיאה בהתחברות")
    def test_failed_login(self, setup_ui):
        with allure.step("קריאת נתוני כשל מהקונפיג"):
            user = ConfigReader.read_config('user_details_failed', 'user')
            password = ConfigReader.read_config('user_details_failed', 'password')

        setup_ui.login_page.fill_page(user, password)

        with allure.step("אימות טקסט הודעת השגיאה"):
            actual_error = setup_ui.login_page.get_error_message()
            expected_error = "Epic sadface: Username and password do not match any user in this service"
            assert actual_error == expected_error, f"Expected error '{expected_error}' but got '{actual_error}'"











