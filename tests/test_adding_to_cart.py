import time

import pytest

from pageobjects.cart_page import CartPage
from pageobjects.home_page import HomePage
from pageobjects.popup_window import PopUpWindow
from utils.base import Base


class TestAddingToCart(Base):

    home_page = HomePage(Base.driver)
    popup_window = PopUpWindow(Base.driver)
    cart_page = CartPage(Base.driver)

    def setup_class(self):
        self.visit(self, "https://demo.litecart.net/en/")

    @pytest.mark.parametrize("item_name, size, quantity", [
        ("Yellow Duck", "Small", "2")
    ])
    def test_scenario(self, item_name, size, quantity):
        self.home_page.choose_item(item_name)
        self.wait_to_be_visible(self.popup_window.popup_window_locator, 3)
        self.popup_window.select_size(size)
        self.popup_window.input_quantity(quantity)
        self.popup_window.add_to_cart()
        self.popup_window.close()
        self.wait_not_visible(self.popup_window.popup_window_locator, 3)
        self.home_page.go_to_cart()
        self.wait_page(self.cart_page, 5)
        assert self.cart_page.check_item_in_cart(item_name, size, quantity)

    def teardown_class(self):
        self.close(self)
