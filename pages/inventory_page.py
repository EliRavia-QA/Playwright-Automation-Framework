import allure

from components.header import Header
from components.sidebar import Sidebar
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar = Sidebar(page)
        self.header = Header(page)

    LIST_ITEMS = ".inventory_list > div"
    ITEM_NAME = ".inventory_item_name"
    BTN_INVENTORY = ".btn_inventory"
    REMOVE_ֹBTN = "button[data-test^='remove-']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    PRODUCT_NAME_LOCATOR = ".inventory_item_name"
    FIRST_ITEM_NAME = "[data-test='inventory-item-name']"
    TITLE = ".title"

    def add_fleece_jacket_to_cart(self):

        self.click_item_by_text_from_list(
            self.LIST_ITEMS,
            self.ITEM_NAME,
            self.BTN_INVENTORY,
            "Sauce Labs Fleece Jacket"
        )

    def add_item_to_cart(self, product_name):
        self.click_item_by_text_from_list(
            self.LIST_ITEMS,
            self.ITEM_NAME,
            self.BTN_INVENTORY,
            product_name
        )

    def remove_product_from_cart(self, product_name):
        self.click_item_by_text_from_list(
            self.LIST_ITEMS,
            self.ITEM_NAME,
            self.REMOVE_ֹBTN,
            product_name
        )

    def sort_products(self, sort_type):
        self.select_from_dropdown(self.SORT_DROPDOWN, sort_type)

    def get_first_item_name(self):
        return self.page.locator(self.FIRST_ITEM_NAME).first.text_content()

    def get_title(self):
        return self.page.inner_text(self.TITLE)

    @allure.step("לחיצה על אייקון העגלה (דרך ה-Header)")
    def click_cart(self):
        self.header.click_cart()

    @allure.step("קבלת מחיר המוצר: {product_name}")
    def get_item_price(self, product_name):
        # מוצא את המחיר בשורת המוצר הספציפי
        selector = f"//div[text()='{product_name}']/../../..//div[@class='inventory_item_price']"
        return self.page.locator(selector).text_content()

    @allure.step("לחיצה על שם המוצר: {product_name}")
    def click_item_name(self, product_name):
        self.page.locator(self.ITEM_NAME, has_text=product_name).click()

    @allure.step("בדיקת הלינק לטוויטר ב-Footer")
    def get_twitter_link(self):
        return self.page.locator(".social_twitter a").get_attribute("href")

    @allure.step("קבלת כמות המוצרים על האייקון של העגלה")
    def get_cart_badge(self):
        return str(self.header.get_cart_count())




