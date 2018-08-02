"""Модуль с шагами для теста Creating customer account"""
from features.steps.steps_adding_to_cart import *


@given('Before creating customer account execute steps of adding item to cart scenario with params: '
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


@when('Set tax id "{tax_id}"')
def step_impl(context, tax_id):
    context.cart_page.send_text_to('tax_id field', tax_id, 3)


@step('Set company "{company}"')
def step_impl(context, company):
    context.cart_page.send_text_to('company field', company, 3)


@step('Set first name "{first_name}"')
def step_impl(context, first_name):
    context.cart_page.send_text_to('first_name field', first_name, 3)


@step('Set last name "{last_name}"')
def step_impl(context, last_name):
    context.cart_page.send_text_to('last_name field', last_name, 3)


@step('Set address1 "{address1}"')
def step_impl(context, address1):
    context.cart_page.send_text_to('address1 field', address1, 3)


@step('Set address2 "{address2}"')
def step_impl(context, address2):
    context.cart_page.send_text_to('address2 field', address2, 3)


@step('Set postcode "{postcode}"')
def step_impl(context, postcode):
    context.cart_page.send_text_to('postcode field', postcode, 3)


@step('Set city "{city}"')
def step_impl(context, city):
    context.cart_page.send_text_to('city field', city, 3)


@step('Set country "{country}"')
def step_impl(context, country):
    context.cart_page.select_item('country field', country, 3)


@step('Set email "{email}"')
def step_impl(context, email):
    context.cart_page.send_text_to('email field', email, 3)


@step('Set phone "{phone}"')
def step_impl(context, phone):
    context.cart_page.send_text_to('phone field', phone, 3)


@step('Select create account checkbox')
def step_impl(context):
    context.cart_page.click_at('create_account_checkbox', 3)


@then('Should open password fields')
def step_impl(context):
    assert context.cart_page.is_visible('desired password field', 3)
    assert context.cart_page.is_visible('confirmed password field', 3)


@step('Set desired password "{desired_password}"')
def step_impl(context, desired_password):
    context.cart_page.send_text_to('desired password field', desired_password, 3)


@step('Set confirmed password "{confirmed_password}"')
def step_impl(context, confirmed_password):
    context.cart_page.send_text_to('confirmed password field', confirmed_password, 3)


@step('Click save changes button')
def step_impl(context):
    context.cart_page.click_at('save changes button', 3)


@then('Should appear account created or account exists alert')
def step_impl(context):
    if not context.cart_page.is_visible('account created alert', 3):
        assert context.cart_page.is_visible('account exists alert', 3)
