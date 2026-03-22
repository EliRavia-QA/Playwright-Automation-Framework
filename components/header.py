class Header:
    def __init__(self, page):
        self.page = page


        self._CART_LINK = ".shopping_cart_link"
        self._CART_BADGE = ".shopping_cart_badge"
        self._MENU_BTN = "#react-burger-menu-btn"
        self._HEADER_LABEL = ".app_logo"

    def get_cart_count(self):
        if self.page.is_visible(self._CART_BADGE):
            return int(self.page.inner_text(self._CART_BADGE))
        return 0

    def click_cart(self):
        self.page.click(self._CART_LINK)

    def get_logo_text(self):
        return self.page.inner_text(self._HEADER_LABEL)
