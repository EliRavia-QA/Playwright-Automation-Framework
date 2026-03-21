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
        with allure.step("קריאת נתוני התחברות מהקונפיג"):
            user = ConfigReader.read_config('user_details', 'user')
            password = ConfigReader.read_config('user_details', 'password')
        with allure.step(f"התחברות למערכת עם משתמש {user}"):
            setup_ui.login_page.fill_page(user, password)
        with allure.step("מעבר לעמוד עגלת הקניות"):
            setup_ui.inventory_page.click_cart()
        with allure.step("תיקוף שהעגלה אינה מכילה מוצרים"):
            items_count = setup_ui.cart_page.get_items_count()
            assert items_count == 0, f"צפוי 0 מוצרים בעגלה, אך נמצאו {items_count}"

    @allure.feature("ניווט באתר")
    @allure.story("זרימת המשך קניות באתר")
    @allure.title("בדיקת כפתור המשך קניות מהעגלה")
    def test_continue_shopping(self, setup_ui):
        with allure.step("הוספת מוצר לעגלה ומעבר לעמוד העגלה"):
            setup_ui.inventory_page.add_item_to_cart("Sauce Labs Backpack")
            setup_ui.inventory_page.click_cart()
        with allure.step("לחיצה על כפתור Continue Shopping"):
            setup_ui.cart_page.click_continue_shopping()






