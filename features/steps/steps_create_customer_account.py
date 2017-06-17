from features.steps.steps_add_to_cart import *


@given('Before creating customer account execute steps of adding item to cart scenario with params: "{browser}", "{item_name}", "{size}", "{quantity}"')
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
    """.format(browser=browser, item_name=item_name, size=size, quantity=quantity))


@when('Set tax id "{tax_id}"')
def step_impl(context, tax_id):
    context.cart_page.set_tax_id(tax_id)


@step('Set company "{company}"')
def step_impl(context, company):
    context.cart_page.set_company(company)

    
@step('Set first name "{first_name}"')
def step_impl(context, first_name):
    context.cart_page.set_first_name(first_name)
    

@step('Set last name "{last_name}"')
def step_impl(context, last_name):
    context.cart_page.set_last_name(last_name)


@step('Set address1 "{address1}"')
def step_impl(context, address1):
    context.cart_page.set_address1(address1)

    
@step('Set address2 "{address2}"')
def step_impl(context, address2):
    context.cart_page.set_address2(address2)
    

@step('Set postcode "{postcode}"')
def step_impl(context, postcode):
    context.cart_page.set_postcode(postcode)
    

@step('Set city "{city}"')
def step_impl(context, city):
    context.cart_page.set_city(city)
    
    
@step('Set country "{country}"')
def step_impl(context, country):
    context.cart_page.set_country(country)
    
    
@step('Set email "{email}"')
def step_impl(context, email):
    context.cart_page.set_email(email)
    
    
@step('Set phone "{phone}"')
def step_impl(context, phone):
    context.cart_page.set_phone(phone)
   
   
@step('Select create account checkbox')
def step_impl(context):
    context.cart_page.select_create_account_checkbox()
    
    
@step('Set desired password "{desired_password}"')
def step_impl(context, desired_password):
    context.cart_page.set_desired_password(desired_password)
    
    
@step('Set confirmed password "{confirmed_password}"')
def step_impl(context, confirmed_password):
    context.cart_page.set_confirmed_password(confirmed_password)


@step('Click save changes button')
def step_impl(context):
    context.cart_page.click_save_changes_button()


@then('Should appear account created alert')
def step_impl(context):
    assert context.cart_page.is_account_created_alert_visible()
    

