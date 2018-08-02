"""Модуль с шагами для теста Confirming order"""
from features.steps.steps_adding_to_cart import *


@given('Before confirming order execute steps of adding item to cart scenario with params: '
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


@given('Before confirming order execute steps for setting customer information with params: "{tax_id}", "{company}", '
       '"{first_name}", "{last_name}", "{address1}", "{address2}", "{postcode}", "{city}", "{country}", "{email}", '
       '"{phone}"')
def step_impl(context, tax_id, company, first_name, last_name, address1, address2, postcode, city, country, email, phone):
    context.execute_steps("""
      When Set tax id "{tax_id}"
        And Set company "{company}"
        And Set first name "{first_name}"
        And Set last name "{last_name}"
        And Set address1 "{address1}"
        And Set address2 "{address2}"
        And Set postcode "{postcode}"
        And Set city "{city}"
        And Set country "{country}"
        And Set email "{email}"
        And Set phone "{phone}"
        And Click save changes button
    """.format(tax_id=tax_id,
               company=company,
               first_name=first_name,
               last_name=last_name,
               address1=address1,
               address2=address2,
               postcode=postcode,
               city=city,
               country=country,
               email=email,
               phone=phone))


@when('Click confirm order button')
def step_impl(context):
    context.cart_page.click_at('confirm order button', 6)


@then('Should appear page with message "{message}"')
def step_impl(context, message):
    assert context.helper.is_page_opened(context.success_order_page, 10)
    assert context.success_order_page.get_text_from('success message', 3) == message
