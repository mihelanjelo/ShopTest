Feature: Confirming order

  Scenario Outline:
      Given Before confirming order execute steps of adding item to cart scenario with params: "<browser>", "<item_name>", "<size>", "<quantity>"
      Given Before confirming order execute steps for setting customer information with params: "<tax_id>", "<company>", "<first_name>", "<last_name>", "<address1>", "<address2>", "<postcode>", "<city>", "<country>", "<email>", "<phone>"
      When Click confirm order button
      Then Should appear page with message "Your order is successfully completed!"

    Examples:
      | browser | item_name    | size  | quantity | tax_id    | company | first_name | last_name | address1 | address2 | postcode | city      | country | email       | phone  |
      | Chrome  | Yellow Duck  | Small | 2        | X12345678 | google  | Leo        | Messi     | Camp Nou | Madrid   | 08001    | Barcelona | Spain   | leo@mail.ru | 123232 |
