import allure

from utils.config import ConfigReader


@allure.epic("בדיקות UI לאתר")
class TestSauceUI:

    @allure.feature("ניהול עגלת קניות")
    @allure.story("בדיקת עגלה ריקה")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("לוודא שהעגלה ריקה לאחר התחברות לאתר")
    @allure.title("בדיקת עגלה ריקה לאחר לוגין")
    def test_empty_cart(self, setup_ui):
        with allure.step("התחברות למערכת"):
            setup_ui.login_page.quick_login()
        with allure.step("מעבר לעמוד עגלת הקניות"):
            setup_ui.inventory_page.click_cart()
        with allure.step("תיקוף שהעגלה אינה מכילה מוצרים"):
            items_count = setup_ui.cart_page.get_items_count()
            assert items_count == 0, f"צפוי 0 מוצרים בעגלה, אך נמצאו {items_count}"

    @allure.feature("ניווט באתר")
    @allure.story("זרימת המשך קניות באתר")
    @allure.title("בדיקת כפתור המשך קניות מהעגלה")
    def test_continue_shopping(self, setup_ui):
        with allure.step("התחברות למערכת"):
            setup_ui.login_page.quick_login()
        with allure.step("הוספת מוצר לעגלה ומעבר לעמוד העגלה"):
            setup_ui.inventory_page.add_item_to_cart("Sauce Labs Backpack")
            setup_ui.inventory_page.click_cart()
        with allure.step("לחיצה על כפתור Continue Shopping"):
            setup_ui.cart_page.click_continue_shopping()

    @allure.feature("Product Details")
    @allure.story("Integrity Check")
    @allure.title("בדיקת התאמת פרטי מוצר")
    def test_product_details_integrity(self, setup_ui):
        with allure.step("התחברות למערכת"):
            setup_ui.login_page.quick_login()
        with allure.step("Get price from main page"):
            expected_price = setup_ui.inventory_page.get_item_price("Sauce Labs Backpack")

        with allure.step("Click on product name"):
            setup_ui.inventory_page.click_item_name("Sauce Labs Backpack")

        with allure.step("Verify price on details page"):
            actual_price = setup_ui.product_details_page.get_price()
            assert actual_price == expected_price, f"Price mismatch! Expected {expected_price} but got {actual_price}"

    @allure.feature("Product Catalog")
    @allure.story("Product Details Integrity")
    @allure.title("בדיקת התאמת מחיר מוצר בין דף הבית לדף הפירוט")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_details_integrity(self, setup_ui):
        setup_ui.login_page.quick_login()
        with allure.step("משיכת מחיר המוצר 'Sauce Labs Backpack' מדף הבית"):
            expected_price = setup_ui.inventory_page.get_item_price("Sauce Labs Backpack")

        with allure.step("לחיצה על שם המוצר למעבר לדף הפירוט"):
            setup_ui.inventory_page.click_item_name("Sauce Labs Backpack")

        with allure.step("משיכת המחיר מתוך דף הפירוט"):
            actual_price = setup_ui.inventory_page.get_price_from_details()

        with allure.step(f"וידוא שהמחיר בדף הפירוט ({actual_price}) זהה למחיר בדף הבית ({expected_price})"):
            assert actual_price.strip() == expected_price.strip(), \
                f"טעות במחיר! צפינו ל-{expected_price} אבל קיבלנו {actual_price}"

    @allure.feature("תהליך רכישה")
    @allure.story("בדיקות ולידציה ושגיאות")
    @allure.title("בדיקת שגיאה כשחסרים פרטי משתמש בצ'ק-אאוט")
    def test_checkout_missing_info_error(self, setup_ui):
        setup_ui.login_page.quick_login()

        with allure.step("הוספת מוצר ומעבר לעגלה"):
            setup_ui.inventory_page.add_item_to_cart("Sauce Labs Backpack")
            setup_ui.inventory_page.click(".shopping_cart_link")

        with allure.step("מעבר לצ'ק-אאוט ולחיצה על המשך ללא פרטים"):
            setup_ui.inventory_page.click("#checkout")
            setup_ui.inventory_page.click("#continue")

        with allure.step("וידוא הופעת הודעת שגיאה על שם חסר"):
            error_msg = setup_ui.login_page.get_error_message()
            assert "First Name is required" in error_msg, f"הודעת השגיאה לא תקינה: {error_msg}"






