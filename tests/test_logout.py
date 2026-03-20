import allure
import pytest
from utils.config import ConfigReader


@allure.epic("ניהול חשבון משתמש")
@allure.feature("התנתקות מהמערכת - Logout")
class TestLogout:

    @allure.story("תהליך התנתקות תקין")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("בדיקת יציאה מהמערכת וחזרה לדף הלוגין")
    @allure.description("טסט זה בודק שהמשתמש יכול להתנתק דרך התפריט הצדדי ושנמנעת ממנו גישה לדף המלאי לאחר מכן")
    def test_logout_flow(self, setup_ui):
        # שימוש ב-setup_ui במקום app בהתאם לפיקסטורה החדשה שלנו

        with allure.step("קריאת פרטי משתמש מקובץ הקונפיגורציה"):
            user = ConfigReader.read_config('user_details', 'user')
            password = ConfigReader.read_config('user_details', 'password')

        with allure.step(f"התחברות למערכת עם המשתמש: {user}"):
            setup_ui.login_page.fill_page(user, password)
            assert setup_ui.inventory_page.get_title() == "Products"

        with allure.step("פתיחת תפריט צדדי וביצוע Logout"):
            setup_ui.inventory_page.sidebar.logout()

        with allure.step("ווידוא חזרה לדף הלוגין"):
            # בדיקה שכפתור הלוגין חזר להיות גלוי
            is_login_visible = setup_ui.login_page.page.is_visible(setup_ui.login_page.LOGIN_BTN)
            assert is_login_visible, "כפתור הלוגין לא מופיע לאחר ההתנתקות"

        with allure.step("ווידוא שה-URL לא מכיל יותר את דף ה-Inventory"):
            current_url = setup_ui.login_page.page.url
            assert "inventory" not in current_url, f"המשתמש עדיין בדף המלאי! URL: {current_url}"
