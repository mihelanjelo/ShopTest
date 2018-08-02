"""Модуль с шагами для теста Adding item to cart"""

from behave import *

from pageobjects.cart_page import CartPage
from pageobjects.home_page import HomePage
from pageobjects.popup_window import PopUpWindow
from pageobjects.success_order_page import SuccessOrderPage
from utils.helper import Helper


@given('Open browser')
def step_impl(context):
    context.helper = Helper(context.browser, context.browser_exe_path)
    context.home_page = HomePage(context.helper.driver)
    context.popup_window = PopUpWindow(context.helper.driver)
    context.cart_page = CartPage(context.helper.driver)
    context.success_order_page = SuccessOrderPage(context.helper.driver)


@when('Go to "{url}"')
def step_impl(context, url):
    context.helper.visit(url)


@step('Click on "{item_name}"')
def step_impl(context, item_name):
    assert context.helper.is_page_opened(context.home_page, 5)
    context.home_page.click_at('item link', 3, values={'item_name': item_name})


@then('Should open pop-up window with item definition')
def step_impl(context):
    assert context.popup_window.is_visible('popup window', 3)


@when('Set size "{size}"')
def step_impl(context, size):
    context.popup_window.select_item('select size', size, 3)


@step('Set quantity "{quantity}"')
def step_impl(context, quantity):
    context.popup_window.send_text_to('quantity field', quantity, 3)


@step('Click add to cart button')
def step_impl(context):
    context.popup_window.click_at('add to cart button', 3)


@step('Close pop-up window')
def step_impl(context):
    context.popup_window.click_at('close popup button', 3)


@then('Should pop-up window close')
def step_impl(context):
    assert context.popup_window.is_not_visible('popup window', 3)


@when('Open shopping cart')
def step_impl(context):
    context.home_page.click_at("go to cart link")


@then('Should cart page open and choose "{item_name}" in list with chosen "{size}" and "{quantity}"')
def step_impl(context, item_name, size, quantity):
    assert context.helper.is_page_opened(context.cart_page, 5)
    assert context.cart_page.is_visible("item in cart", 4,
                                        values={'item_name': item_name, 'size': size, 'quantity': quantity})
