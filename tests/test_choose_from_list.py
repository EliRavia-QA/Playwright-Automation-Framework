# tests/test_inventory.py

import allure
import pytest


@allure.epic("ניהול מלאי ומוצרים")
@allure.feature("חנות SauceDemo - Inventory")
class TestInventory:

    @allure.story("הוספת מוצר בודד לעגלה")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("בדיקת הוספת מעיל (Fleece Jacket) לעגלה")
    def test_add_fleece_to_cart(self, setup_ui):
        with allure.step("התחברות למערכת"):
            setup_ui.login_page.fill_page("standard_user", "secret_sauce")

        with allure.step("הוספת מעיל Fleece לעגלה"):
            setup_ui.inventory_page.add_fleece_jacket_to_cart()

        with allure.step("ווידוא שהעגלה התעדכנה ל-1"):
            cart_badge = setup_ui.page.locator("[data-test='shopping-cart-badge']")
            assert cart_badge.text_content() == "1"

    @allure.story("מחיקת מוצר מהעגלה")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("הוספה ומחיקה של מוצר מהעגלה")
    def test_remove_fleece_from_cart(self, setup_ui):
        with allure.step("התחברות והוספת מוצר"):
            setup_ui.login_page.fill_page("standard_user", "secret_sauce")
            setup_ui.inventory_page.add_any_product("Sauce Labs Fleece Jacket")

        with allure.step("ווידוא הוספה ומחיקה"):
            assert setup_ui.page.locator("[data-test='shopping-cart-badge']").text_content() == "1"
            setup_ui.inventory_page.remove_product_from_cart("Sauce Labs Fleece Jacket")

        with allure.step("ווידוא שהעגלה ריקה"):
            cart_badge = setup_ui.page.locator("[data-test='shopping-cart-badge']")
            assert cart_badge.count() == 0

    @allure.story("הוספת מספר מוצרים")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("בדיקת הוספת 3 מוצרים שונים לעגלה")
    def test_add_number_of_products(self, setup_ui):
        setup_ui.login_page.fill_page("standard_user", "secret_sauce")
        products_to_add = ["Sauce Labs Fleece Jacket", "Sauce Labs Backpack", "Sauce Labs Bike Light"]

        for product in products_to_add:
            with allure.step(f"הוספת מוצר: {product}"):
                setup_ui.inventory_page.add_any_product(product)

        with allure.step("ווידוא כמות מוצרים בעגלה"):
            expected_count = str(len(products_to_add))
            assert setup_ui.page.locator("[data-test='shopping-cart-badge']").text_content() == expected_count

    @allure.story("פונקציונליות UI - גלילה")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("בדיקת גלילה בדף המוצרים")
    def test_scroll_inventory(self, setup_ui):
        setup_ui.login_page.fill_page("standard_user", "secret_sauce")
        with allure.step("ביצוע גלילה למטה ב-500 פיקסלים"):
            setup_ui.inventory_page.scroll_by_amount(0, 500)

    @allure.story("מיון מוצרים")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("מיון מהמחיר הנמוך לגבוה")
    def test_sort_product_price_low_to_high(self, setup_ui):
        setup_ui.login_page.fill_page("standard_user", "secret_sauce")
        with allure.step("מיון לפי מחיר: מהנמוך לגבוה"):
            setup_ui.inventory_page.sort_products("Price (low to high)")

        with allure.step("ווידוא שהמחיר הראשון הוא 7.99$"):
            first_item_price = setup_ui.page.locator(".inventory_item_price").first.text_content()
            assert first_item_price == "$7.99"

    @allure.story("מיון מוצרים")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("מיון מהמחיר הגבוה לנמוך")
    def test_sort_product_price_high_to_low(self, setup_ui):
        setup_ui.login_page.fill_page("standard_user", "secret_sauce")
        with allure.step("מיון לפי מחיר: מהגבוה לנמוך"):
            setup_ui.inventory_page.sort_products("Price (high to low)")

        with allure.step("ווידוא שהמחיר הראשון הוא 49.99$"):
            first_item_price = setup_ui.page.locator('[data-test="inventory-item-price"]').first.text_content()
            assert first_item_price == "$49.99"

    @allure.story("מיון מוצרים")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("מיון אלפביתי הפוך (Z to A)")
    def test_sort_products_z_to_a(self, setup_ui):
        setup_ui.login_page.fill_page("standard_user", "secret_sauce")
        with allure.step("מיון לפי שם: Z עד A"):
            setup_ui.inventory_page.sort_products("Name (Z to A)")

        with allure.step("ווידוא שם המוצר הראשון"):
            expected_name = "Test.allTheThings() T-Shirt (Red)"
            actual_name = setup_ui.inventory_page.get_first_item_name()
            assert actual_name == expected_name, f"Expected {expected_name} but got {actual_name}"


   








