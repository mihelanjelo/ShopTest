Feature: Shopping cart basic feature

  Background:
      When Go to "https://demo.litecart.net/en/"

  Scenario Outline: Adding item to cart
      When Click on "<item>"
      Then Should open pop-up window with item definition
      When Set size "<size>"
        And Set quantity "<quantity>"
        And Click add to cart button
        And Close pop-up window
      Then Should pop-up window close
      When Open shopping cart
      Then Should cart page open and choose "<item>" in list with chosen "<size>" and "<quantity>"
      When Click delete "<item>" from list
      Then Should item with params: "<item_name>", "<size>", "<quantity>" disappear


      Examples:
       | item         | size  | quantity |
       | Yellow Duck  | Small | 2        |


  Scenario Outline: Changing quantity of item in cart
      Given Before changing cart item quantity execute steps of adding item to cart scenario with params: "<item_name>", "<size>", "<quantity>"
      When Select for item "<item_name>" new quantity "<new_quantity>"
        And Remember sum of "<item_name>"
        And Click refresh item "<item_name>" button
      Then Should quantity "<quantity>" of "<item_name>" change to "<new_quantity>" and sum must be proportional increase or decrease, page load time max "5" sec
      When Click delete "<item_name>" from list
      Then Should item with params: "<item_name>", "<size>", "<quantity>" disappear


      Examples:
       | item_name    | size  | quantity | new_quantity |
       | Yellow Duck  | Small | 2        | 3            |


  Scenario Outline: Confirming order
      Given Before confirming order execute steps of adding item to cart scenario with params: "<item_name>", "<size>", "<quantity>"
      Given Before confirming order execute steps for setting customer information with params: "<tax_id>", "<company>", "<first_name>", "<last_name>", "<address1>", "<address2>", "<postcode>", "<city>", "<country>", "<email>", "<phone>"
      When Click confirm order button
      Then Should appear page with message "Your order is successfully completed!"
      When Click delete "<item_name>" from list
      Then Should item with params: "<item_name>", "<size>", "<quantity>" disappear

    Examples:
      | item_name    | size  | quantity | tax_id    | company | first_name | last_name | address1 | address2 | postcode | city      | country | email       | phone  |
      | Yellow Duck  | Small | 2        | X12345678 | google  | Leo        | Messi     | Camp Nou | Madrid   | 08001    | Barcelona | Spain   | leo@mail.ru | 123232 |


  Scenario Outline: Creating customer account
      Given Before creating customer account execute steps of adding item to cart scenario with params: "<item_name>", "<size>", "<quantity>"
      When Set tax id "<tax_id>"
        And Set company "<company>"
        And Set first name "<first_name>"
        And Set last name "<last_name>"
        And Set address1 "<address1>"
        And Set address2 "<address2>"
        And Set postcode "<postcode>"
        And Set city "<city>"
        And Set country "<country>"
        And Set email "<email>"
        And Set phone "<phone>"
        And Select create account checkbox
      Then Should open password fields
      When Set desired password "<desired_password>"
        And Set confirmed password "<confirmed_password>"
        And Click save changes button
      Then Should appear account created or account exists alert

    Examples:
      | item_name    | size  | quantity | tax_id    | company | first_name | last_name | desired_password | confirmed_password | address1 | address2 | postcode | city      | country | email       | phone  |
      | Yellow Duck  | Small | 2        | X12345678 | google  | Leo        | Messi     | barca10          | barca10            | Camp Nou | Madrid   | 08001    | Barcelona | Spain   | leo@mail.ru | 123232 |


  Scenario Outline: Removing item from cart
      Given Before deleting item execute steps of adding item to cart scenario with params: "<item_name>", "<size>", "<quantity>"
      When Click delete "<item_name>" from list
      Then Should item with params: "<item_name>", "<size>", "<quantity>" disappear

    Examples:
      | item_name    | size  | quantity |
      | Yellow Duck  | Small | 2        |