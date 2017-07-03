from features.steps.steps_adding_to_cart import *


@given(
    'Before creating customer account execute steps of adding item to cart scenario with params: "{browser}", "{item_name}", "{size}", "{quantity}"')
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


@when('Set tax id "{tax_id}"')
def step_impl(context, tax_id):
    context.cart_page.set_tax_id(tax_id, 3)


@step('Set company "{company}"')
def step_impl(context, company):
    context.cart_page.set_company(company, 3)


@step('Set first name "{first_name}"')
def step_impl(context, first_name):
    context.cart_page.set_first_name(first_name, 3)


@step('Set last name "{last_name}"')
def step_impl(context, last_name):
    context.cart_page.set_last_name(last_name, 3)


@step('Set address1 "{address1}"')
def step_impl(context, address1):
    context.cart_page.set_address1(address1, 3)


@step('Set address2 "{address2}"')
def step_impl(context, address2):
    context.cart_page.set_address2(address2, 3)


@step('Set postcode "{postcode}"')
def step_impl(context, postcode):
    context.cart_page.set_postcode(postcode, 3)


@step('Set city "{city}"')
def step_impl(context, city):
    context.cart_page.set_city(city, 3)


@step('Set country "{country}"')
def step_impl(context, country):
    context.cart_page.set_country(country, 3)


@step('Set email "{email}"')
def step_impl(context, email):
    context.cart_page.set_email(email, 3)


@step('Set phone "{phone}"')
def step_impl(context, phone):
    context.cart_page.set_phone(phone, 3)


@step('Select create account checkbox')
def step_impl(context):
    context.cart_page.select_create_account_checkbox(3)


@then('Should open password fields')
def step_impl(context):
    desired_password_field = context.helper.wait_to_be_visible(context.cart_page.desired_password_field_locator, 5)
    confirmed_password_field = context.helper.wait_to_be_visible(context.cart_page.confirmed_password_field_locator, 5)
    assert desired_password_field != False
    assert confirmed_password_field != False


@step('Set desired password "{desired_password}"')
def step_impl(context, desired_password):
    context.cart_page.set_desired_password(desired_password, 3)


@step('Set confirmed password "{confirmed_password}"')
def step_impl(context, confirmed_password):
    context.cart_page.set_confirmed_password(confirmed_password, 3)


@step('Click save changes button')
def step_impl(context):
    context.cart_page.click_save_changes_button(3)


@then('Should appear account created or account exists alert')
def step_impl(context):
    account_exists_alert = context.helper.wait_to_be_visible(context.cart_page.account_exists_alert_locator, 5)
    account_created_alert = context.helper.wait_to_be_visible(context.cart_page.account_created_alert_locator, 5)
    if account_created_alert == False:
        assert account_exists_alert != False

