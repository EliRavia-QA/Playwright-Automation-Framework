import allure
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    USER_NAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    @allure.step("הזנת פרטי התחברות: שם משתמש '{user_name}' וסיסמה '{password}'")
    def fill_page(self, user_name, password):
        self.fill_text(self.USER_NAME_FIELD, user_name)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    @allure.step("קבלת הודעת השגיאה מהדף")
    def get_error_message(self):
        return self.page.inner_text(self.ERROR_MESSAGE)












