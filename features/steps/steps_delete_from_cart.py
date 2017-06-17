from features.steps.steps_add_to_cart import *


@given('Executed steps of adding item to cart scenario with params: "{browser}", "{item_name}", "{size}", "{quantity}"')
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


@when('Click delete "{item_name}" from list')
def step_impl(context, item_name):
    context.cart_page.delete_item(item_name)


@then('Item "{item_name}", "{size}", "{quantity}" disappears')
def step_impl(context, item_name, size, quantity):
    assert context.cart_page.check_item_not_in_cart(item_name, size, quantity)
