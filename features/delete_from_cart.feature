Feature: Removing item from cart

  Scenario Outline:
      Given Executed steps of adding item to cart scenario with params: "<browser>", "<item_name>", "<size>", "<quantity>"
      When Click delete "<item_name>" from list
      Then Item "<item_name>", "<size>", "<quantity>" disappears


    Examples:
      | browser | item_name    | size  | quantity |
      | Chrome  | Yellow Duck  | Small | 2        |