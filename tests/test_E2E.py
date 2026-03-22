import allure
import pytest
from utils.config import ConfigReader


@allure.epic("תהליכים עסקיים מקצה לקצה")
@allure.feature("רכישת מוצרים - E2E")
class TestE2E:

    @allure.story("תהליך רכישה בסיסי מוצלח")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("בדיקת זרימה מלאה: התחברות, הוספה לסל ומעבר לעגלה")
    @allure.description(
        "טסט זה מוודא את הליבה של האתר: כניסת משתמש, בחירת מוצר ספציפי ווידוא שהמוצר מופיע בעגלת הקניות")
    def test_complete_purchase_flow(self, setup_ui):

        with allure.step("טעינת פרטי הזדהות מקובץ Config"):
            user = ConfigReader.read_config('user_details', 'user')
            password = ConfigReader.read_config('user_details', 'password')

        with allure.step(f"ביצוע Login עם משתמש: {user}"):
            setup_ui.login_page.fill_page(user, password)
            assert "inventory" in setup_ui.page.url, "שגיאה: המשתמש לא הועבר לדף המלאי לאחר התחברות"

        target_product = "Sauce Labs Backpack"
        with allure.step(f"בחירת מוצר: {target_product} והוספתו לסל"):
            setup_ui.inventory_page.add_item_to_cart(target_product)

        with allure.step("ווידוא עדכון מונה העגלה ב-Header"):
            cart_count = setup_ui.inventory_page.header.get_cart_count()
            assert cart_count == 1, f"צפוי מוצר אחד בעגלה, אך נמצאו: {cart_count}"

        with allure.step("מעבר לעמוד עגלת הקניות"):
            setup_ui.inventory_page.header.click_cart()
            assert "cart.html" in setup_ui.page.url, "שגיאה: המעבר לעמוד העגלה נכשל"