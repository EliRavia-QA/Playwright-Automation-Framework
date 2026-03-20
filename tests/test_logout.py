from utils.config import ConfigReader


class TestLogout:

    def test_logout_flow(self, app):
        user = ConfigReader.read_config('user_details', 'user')
        password = ConfigReader.read_config('user_details', 'password')
        app.login_page.fill_page(user, password)
        assert app.inventory_page.get_title() == "Products"
        app.inventory_page.sidebar.logout()
        assert app.login_page.page.is_visible(app.login_page.LOGIN_BTN), "Login button is not visible after logout"
        current_url = app.login_page.page.url
        assert "inventory" not in current_url, f"Still on inventory page! URL: {current_url}"
