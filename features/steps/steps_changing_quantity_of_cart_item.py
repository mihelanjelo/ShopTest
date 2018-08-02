import time
from features.steps.steps_adding_to_cart import *


@given('Before changing cart item quantity execute steps of adding item to cart scenario with params: '
       '"{item_name}", "{size}", "{quantity}"')
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


@when('Select for item "{item_name}" new quantity "{new_quantity}"')
def step_impl(context, item_name, new_quantity):
    context.cart_page.send_text_to('change item quantity field', new_quantity, 3, values={'item_name': item_name})


@step('Remember sum of "{item_name}"')
def step_impl(context, item_name):
    text = context.cart_page.get_text_from('item sum field', 3, values={'item_name': item_name})
    context.item_sum = round(float(text.replace("$", "")), 2)


@step('Click refresh item "{item_name}" button')
def step_impl(context, item_name):
    context.cart_page.click_at('item refresh button', 3, values={'item_name': item_name})


@then('Should quantity "{quantity}" of "{item_name}" change to "{new_quantity}" and sum must be proportional increase '
      'or decrease, page load time max "{load_time}" sec')
def step_impl(context, item_name, quantity, new_quantity, load_time):
    ok = False
    for i in range(0, (int(load_time) * 2) + 1):
        text = context.cart_page.get_text_from('item sum field', 3, values={'item_name': item_name})
        if round(float(text.replace("$", "")), 2) == context.item_sum / int(quantity) * int(new_quantity):
            ok = True
            break
        time.sleep(0.5)
    assert ok

