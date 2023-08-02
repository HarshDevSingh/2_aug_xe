Feature: Xe.com currency conversion tests

  Scenario Outline: Test currency conversion on xe
    Given I am on xe.com currency conversion page
    And I accept cookies
    And I close modal
    And I enter <from_amount>
    And I select <from_currency> source
    And I select target <to_currency>
    When I submit currency pair to get conversion rate
    Then I should see correct data for "form" and "to" currency on conversion result page
    Examples: currency conversion pair
   | from_currency | to_currency | from_amount |
   |      AED      |    INR      |   13900.00  |
   |      RUB      |    EUR      |   16900.20  |
   |      EUR      |    AED      |   17956.90  |
   |      EUR      |    RUB      |   57956.90  |
   |      INR      |    RUB      |   87956.90  |


