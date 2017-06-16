from behave import given, when, then
from selenium.common.exceptions import WebDriverException
from features.steps.steps_add_to_cart import *


@given('Executed steps of basic scenario with params: "{browser}", "{item_name}", "{size}", "{quantity}"')
def step_impl(context, browser, item_name, size, quantity):
    context.execute_steps("""
      Given Open "{browser}"
      When Go to "https://demo.litecart.net/en/"
         And Click on "{item}"
      Then See pop-up window with item definition
      When Set size "{size}"
        And Set quantity "{quantity}"
        And Click add to cart button
        And Close pop-up window
      Then Pop-up window is closed
      When Open shopping cart
      Then Cart page is opened and chosen "{item}" in list with chosen "{size}" and "{quantity}"
    """.format(browser=browser, item=item_name, size=size, quantity=quantity))


@when('Click delete item from list button')
def step_impl(context):
    context.cart_page.delete_item()


@then('Item "{item_name}", "{size}", "{quantity}" disappears')
def step_impl(context, item_name, size, quantity):
    check = False
    for i in range(0, 11):
        try:
            context.cart_page.check_item_in_cart(item_name, size, quantity)
        except WebDriverException:
            check = True
            break
        time.sleep(0.5)
    assert check
