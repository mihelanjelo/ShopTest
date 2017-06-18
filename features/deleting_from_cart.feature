Feature: Removing item from cart

  Scenario Outline:
      Given Before deleting item execute steps of adding item to cart scenario with params: "<browser>", "<item_name>", "<size>", "<quantity>"
      When Click delete "<item_name>" from list
      Then Should item with params: "<item_name>", "<size>", "<quantity>" disappear


    Examples:
      | browser | item_name    | size  | quantity |
      | Chrome  | Yellow Duck  | Small | 2        |
