import time

import pytest

from pageobjects.cart_page import CartPage
from pageobjects.home_page import HomePage
from pageobjects.popup_window import PopUpWindow
from utils.helper import Helper


class TestAddingToCart:
    helper = None
    home_page = None      
    popup_window = None
    cart_page = None

    def setup_class(self, browser_name="Chrome"):
        self.helper = Helper(browser_name)
        self.home_page = HomePage(self.helper.driver)
        self.popup_window = PopUpWindow(self.helper.driver)
        self.cart_page = CartPage(self.helper.driver)
        self.helper.visit("https://demo.litecart.net/en/")

    @pytest.mark.parametrize("item_name, size, quantity", [
        ("Yellow Duck", "Small", "2")
    ])
    def test_scenario(self, item_name, size, quantity):
        self.home_page.choose_item(item_name, 3)
        self.helper.wait_to_be_visible(self.popup_window.popup_window_locator, 3)
        self.popup_window.select_size_by_value(size, 3)
        self.popup_window.input_quantity(quantity, 3)
        self.popup_window.add_to_cart(3)
        self.popup_window.close(3)
        self.helper.wait_not_visible(self.popup_window.popup_window_locator, 3)
        self.home_page.go_to_cart(3)
        self.helper.wait_page(self.cart_page, 5)
        assert self.cart_page.check_item_in_cart(item_name, size, quantity, 3)

    def teardown_class(self):
        self.helper.close()
