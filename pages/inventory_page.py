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

    def add_any_product(self, product_name):
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


