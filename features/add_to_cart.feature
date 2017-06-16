Feature: Shopping cart basic test
  
  Scenario Outline: Adding item to cart
      Given Open "<browser>"
      When Go to "https://demo.litecart.net/en/"
      And Click on "<item>"
      Then See pop-up window with item definition
      When Set size "<size>"
      And Set quantity "<quantity>"
      And Click add to cart button
      And Close pop-up window
      Then Pop-up window closed
      When Open shopping cart
      Then Cart page is opened and chosen "<item>" in list with chosen "<size>" and "<quantity>"

      Examples:
       | browser    | item         | size  | quantity |
       | Chrome     | Yellow Duck  | Small | 2        |

