
import allure
from playwright.sync_api import Page

from utils.config import ConfigReader


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("לחיצה על האלמנט: {locator}")
    def click(self, locator):
        self.page.locator(locator).click()

    @allure.step("הקלדת הטקסט '{txt}' לתוך האלמנט: {locator}")
    def fill_text(self, locator, txt):
        self.page.locator(locator).fill(txt)

    @allure.step("קבלת טקסט מהאלמנט: {locator}")
    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    @allure.step("גלילה בדף (X: {x}, Y: {y})")
    def scroll_by_amount(self, x=0, y=500):
        self.page.mouse.wheel(x, y)

    @allure.step("חיפוש ולחיצה על פריט עם הטקסט '{target_text}' בתוך רשימה")
    def click_item_by_text_from_list(self, list_locator, name_locator, button_locator, target_text):
        products_list = self.page.locator(list_locator)
        count = products_list.count()
        for i in range(count):
            current_item = products_list.nth(i)
            title_label = current_item.locator(name_locator).inner_text()


            with allure.step(f"בדיקת פריט מס' { i +1}: {title_label}"):
                if title_label == target_text:
                    with allure.step(f"נמצאה התאמה! לוחץ על כפתור: {button_locator}"):
                        add_to_cart_btn = current_item.locator(button_locator)
                        add_to_cart_btn.click()
                        self.page.wait_for_timeout(2000)
                    break

    @allure.step("בחירה מהתפריט {selector} לפי הערך/טקסט: {value_or_text}")
    def select_from_dropdown(self, selector, value_or_text):
        self.page.wait_for_timeout(2000)
        self.page.locator(selector).select_option(value_or_text)

    @allure.step("המתנה לפתיחת דף חדש לאחר פעולה")
    def wait_for_new_page(self, trigger_action):
        with self.page.context.expect_page() as new_page_info:
            trigger_action()
        return new_page_info.value

    @allure.step("ביצוע התחברות מהירה (Quick Login) מתוך ה-BasePage")
    def quick_login(self):

        user = ConfigReader.read_config('user_details', 'user')
        password = ConfigReader.read_config('user_details', 'password')


        self.fill_text("#user-name", user)
        self.fill_text("#password", password)
        self.click("#login-button")




