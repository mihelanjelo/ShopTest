from features.steps.steps_adding_to_cart import *

item_sum = None


@given('Before changing cart item quantity execute steps of adding item to cart scenario with params: "{browser}", "{item_name}", "{size}", "{quantity}"')
def step_impl(context, browser, item_name, size, quantity):
    context.execute_steps("""
      Given Open "{browser}"
      When Go to "https://demo.litecart.net/en/"
        And Click on "{item_name}"
      Then Should open pop-up window with item definition
      When Set size "{size}"
        And Set quantity "{quantity}"
        And Click add to cart button
        And Close pop-up window
      Then Should pop-up window close
      When Open shopping cart
      Then Should cart page open and choose "{item_name}" in list with chosen "{size}" and "{quantity}"
    """.format(browser=browser,
               item_name=item_name,
               size=size,
               quantity=quantity))


@when('Select for item "{item_name}" new quantity "{new_quantity}"')
def step_impl(context, item_name, new_quantity):
    context.cart_page.change_item_quantity(item_name, new_quantity, 3)


@step('Remember sum of "{item_name}"')
def step_impl(context, item_name):
    context.item_sum = context.cart_page.get_item_sum(item_name, 3)


@step('Click refresh item "{item_name}" button')
def step_impl(context, item_name):
    context.cart_page.click_refresh_item_button(item_name, 3)


@then('Should quantity "{quantity}" of "{item_name}" change to "{new_quantity}" and sum must be proportional increase or decrease, page load time max "{load_time}" sec')
def step_impl(context, item_name, quantity, new_quantity, load_time):
    for i in range(0, (int(load_time) * 2) + 1):
        if context.cart_page.get_item_sum(item_name, 3) == context.item_sum / int(quantity) * int(new_quantity):
            break
        time.sleep(0.5)
    assert context.cart_page.get_item_sum(item_name, 3) == context.item_sum / int(quantity) * int(new_quantity)

