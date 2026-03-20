import pytest

from utils.config import ConfigReader


class TestE2E:

    def test_complete_purchase_flow(self, app):
        user = ConfigReader.read_config('user_details', 'user')
        password = ConfigReader.read_config('user_details', 'password')
        app.login_page.fill_page(user, password)
        assert "inventory" in app.page.url, "Failed to login: URL does not contain 'inventory'"
        target_product = "Sauce Labs Backpack"
        app.inventory_page.add_any_product(target_product)
        cart_count = app.inventory_page.header.get_cart_count()
        assert cart_count == 1, f"Expected 1 item in cart badge, but found {cart_count}"
        app.inventory_page.header.click_cart()
        assert "cart.html" in app.page.url, "Failed to navigate to Cart page"
