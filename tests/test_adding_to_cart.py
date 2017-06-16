import time

import pytest

from pageobjects.cart_page import CartPage
from pageobjects.home_page import HomePage
from pageobjects.popup_window import PopUpWindow
from utils.base import Base


class TestAddingToCart:
    base = None
    home_page = None
    popup_window = None
    cart_page = None

    def setup_class(self, browser_name="Chrome"):
        self.base = Base(browser_name)
        self.home_page = HomePage(self.base.driver)
        self.popup_window = PopUpWindow(self.base.driver)
        self.cart_page = CartPage(self.base.driver)
        self.base.visit("https://demo.litecart.net/en/")

    @pytest.mark.parametrize("item_name, size, quantity", [
        ("Yellow Duck", "Small", "2")
    ])
    def test_scenario(self, item_name, size, quantity):
        self.home_page.choose_item(item_name)
        self.base.wait_to_be_visible(self.popup_window.popup_window_locator, 3)
        self.popup_window.select_size_by_value(size)
        self.popup_window.input_quantity(quantity)
        self.popup_window.add_to_cart()
        self.popup_window.close()
        self.base.wait_not_visible(self.popup_window.popup_window_locator, 3)
        self.home_page.go_to_cart()
        self.base.wait_page(self.cart_page, 5)
        assert self.cart_page.check_item_in_cart(item_name, size, quantity)

    def teardown_class(self):
        self.base.close()
