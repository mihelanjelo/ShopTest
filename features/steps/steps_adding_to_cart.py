import time
from behave import *

from pageobjects.cart_page import CartPage
from pageobjects.home_page import HomePage
from pageobjects.popup_window import PopUpWindow
from pageobjects.success_order_page import SuccessOrderPage
from utils.helper import Helper

helper = None
home_page = None
popup_window = None
cart_page = None
success_order_page = None


@given('Open "{browser}"')
def step_impl(context, browser):
    context.helper = Helper(browser)
    context.home_page = HomePage(context.helper.driver)
    context.popup_window = PopUpWindow(context.helper.driver)
    context.cart_page = CartPage(context.helper.driver)
    context.success_order_page = SuccessOrderPage(context.helper.driver)


@when('Go to "{url}"')
def step_impl(context, url):
    context.helper.visit(url)


@step('Click on "{item_name}"')
def step_impl(context, item_name):
    context.helper.wait_page(context.home_page, 3)
    context.home_page.choose_item(item_name)


@then('Should open pop-up window with item definition')
def step_impl(context):
    context.helper.wait_to_be_visible(context.popup_window.popup_window_locator, 3)


@when('Set size "{size}"')
def step_impl(context, size):
    context.popup_window.select_size_by_value(size)


@step('Set quantity "{quantity}"')
def step_impl(context, quantity):
    context.popup_window.input_quantity(quantity)


@step('Click add to cart button')
def step_impl(context):
    context.popup_window.add_to_cart()


@step('Close pop-up window')
def step_impl(context):
    context.popup_window.close()


@then('Should pop-up window close')
def step_impl(context):
    context.helper.wait_not_visible(context.popup_window.popup_window_locator, 3)


@when('Open shopping cart')
def step_impl(context):
    context.home_page.go_to_cart()


@then('Should cart page open and choose "{item_name}" in list with chosen "{size}" and "{quantity}"')
def step_impl(context, item_name, size, quantity):
    context.helper.wait_page(context.cart_page, 5)
    assert context.cart_page.check_item_in_cart(item_name, size, quantity)
