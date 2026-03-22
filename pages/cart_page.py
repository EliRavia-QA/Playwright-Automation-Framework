import allure
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._CART_ITEM = ".cart_item"
        self._CHECKOUT_BTN = "#checkout"
        self._CONTINUE_SHOPPING_BTN = "#continue-shopping"

    @allure.step("קבלת כמות המוצרים בעגלה")
    def get_items_count(self):
        # הפונקציה שהטסט שלך חיפש ולא מצא
        return self.page.locator(self._CART_ITEM).count()

    @allure.step("לחיצה על Checkout")
    def click_checkout(self):
        self.page.click(self._CHECKOUT_BTN)

    @allure.step("לחיצה על Continue Shopping")
    def click_continue_shopping(self):
        self.page.click(self._CONTINUE_SHOPPING_BTN)