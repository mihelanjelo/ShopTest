Feature: Removing item from cart

  Scenario Outline:
      Given Executed steps of basic scenario with params: "<browser>", "<item_name>", "<size>", "<quantity>"
      When Click delete item from list button
      Then Item "<item_name>", "<size>", "<quantity>" disappears


    Examples:
      | browser | item_name    | size  | quantity |
      | Chrome  | Yellow Duck  | Small | 2        |