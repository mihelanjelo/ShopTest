Feature: Changing quantity of item in cart

  Scenario Outline:
      Given Before changing cart item quantity execute steps of adding item to cart scenario with params: "<browser>", "<item_name>", "<size>", "<quantity>"
      When Select for item "<item_name>" new quantity "<new_quantity>"
        And Remember sum of "<item_name>"
        And Click refresh item "<item_name>" button
      Then Should quantity "<quantity>" of "<item_name>" change to "<new_quantity>" and sum must be proportional increase or decrease, page load time max "5" sec


    Examples:
      | browser | item_name    | size  | quantity | new_quantity |
      | Chrome  | Yellow Duck  | Small | 2        | 3            |