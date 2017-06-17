Feature: Creating customer account

  Scenario Outline:
      Given Before creating customer account execute steps of adding item to cart scenario with params: "<browser>", "<item_name>", "<size>", "<quantity>"
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
        And Set desired password "<desired_password>"
        And Set confirmed password "<confirmed_password>"
        And Click save changes button
      Then Should appear account created alert

    Examples:
      | browser | item_name    | size  | quantity | tax_id | company | first_name | last_name | desired_password | confirmed_password | address1 | address2 | postcode | city      | country   | email       | phone  |
      | Chrome  | Yellow Duck  | Small | 2        | 123    | google  | Leo        | Messi     | barca10          | barca10            | Camp Nou | Madrid   | 55       | Barcelona | Argentina | leo@mail.ru | 123232 |
