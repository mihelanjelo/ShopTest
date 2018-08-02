"""Модуль с шагами для теста Removing item from cart"""
import time
from features.steps.steps_adding_to_cart import *


@given(
    'Before deleting item execute steps of adding item to cart scenario with params: "{item_name}", '
    '"{size}", "{quantity}"')
def step_impl(context, item_name, size, quantity):
    context.execute_steps("""
      When Click on "{item_name}"
      Then Should open pop-up window with item definition
      When Set size "{size}"
        And Set quantity "{quantity}"
        And Click add to cart button
        And Close pop-up window
      Then Should pop-up window close
      When Open shopping cart
      Then Should cart page open and choose "{item_name}" in list with chosen "{size}" and "{quantity}"
    """.format(item_name=item_name,
               size=size,
               quantity=quantity))


@when('Click delete "{item_name}" from list')
def step_impl(context, item_name):
    context.cart_page.click_at('delete item from cart button', 3, values={'item_name': item_name})


@then('Should item with params: "{item_name}", "{size}", "{quantity}" disappear')
def step_impl(context, item_name, size, quantity):
    assert context.cart_page.is_not_visible("item in cart", 4,
                                            values={'item_name': item_name, 'size': size, 'quantity': quantity})
    time.sleep(3)
