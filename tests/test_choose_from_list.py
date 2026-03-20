# tests/test_inventory.py

class TestInventory:

##### בחירת מוצר בודד
    def test_add_fleece_to_cart(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        app.inventory_page.add_fleece_jacket_to_cart()
        cart_badge = app.page.locator("[data-test='shopping-cart-badge']")
        assert cart_badge.text_content() == "1"

#### מחיקת מוצר שהוספתי לעגלת הקניות
    def test_remove_fleece_from_cart(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        app.inventory_page.add_any_product("Sauce Labs Fleece Jacket")
        assert app.page.locator("[data-test='shopping-cart-badge']").text_content() == "1"
        app.inventory_page.remove_product_from_cart("Sauce Labs Fleece Jacket")
        cart_badge = app.page.locator("[data-test='shopping-cart-badge']")
        assert cart_badge.count() == 0

### בחירת מספר מוצרים לעגלת קניות
    def test_add_number_of_products(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        products_to_add = ["Sauce Labs Fleece Jacket", "Sauce Labs Backpack", "Sauce Labs Bike Light"]
        for product in products_to_add:
            app.inventory_page.add_any_product(product)
        expected_count = str(len(products_to_add))
        assert app.page.locator("[data-test='shopping-cart-badge']").text_content() == expected_count

### scroll עם העכבר
    def test_scroll_inventory(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        app.inventory_page.scroll_by_amount(0, 500)


###מיון מוצרים מהמחיר הנמוך לגבוה
    def test_sort_product_price(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        app.inventory_page.sort_products("Price (low to high)")
        first_item_price = app.page.locator(".inventory_item_price").first.text_content()
        assert first_item_price == "$7.99"

###מיון מוצרים מהמחיר הגבוה לנמוך
    def test_sort_product_price2(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        app.inventory_page.sort_products("Price (high to low)")
        first_item_price = app.page.locator('[data-test="inventory-item-price"]').first.text_content()
        assert first_item_price == "$49.99"

### מיון מוצרים לפי סדר הא' ב'
    def test_sort_products_z_to_a(self, app):
        app.login_page.fill_page("standard_user", "secret_sauce")
        app.inventory_page.sort_products("Name (Z to A)")
        expected_name = "Test.allTheThings() T-Shirt (Red)"
        actual_name = app.inventory_page.get_first_item_name()
        assert actual_name == expected_name, f"Expected {expected_name} but got {actual_name}"


   








