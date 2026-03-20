

class Sidebar:
    def __init__(self, page):
        self.page = page


        self._MENU_BTN = "#react-burger-menu-btn"
        self._LOGOUT_LINK = "#logout_sidebar_link"
        self._ALL_ITEMS_LINK = "#inventory_sidebar_link"

    def logout(self):
        self.page.click(self._MENU_BTN)
        self.page.click(self._LOGOUT_LINK)