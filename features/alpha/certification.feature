Feature: Verify add new certification
  Background: Common step
      Given login success with user "ec00003" and pwd "123456789"
      When click Nhan su field
      And click Ho so nhan su field
      And go to page 10
      And click user Le Nam
      And click Certification field
      Then click Add new button

  @c1
  Scenario: add certification successful
    When fill all parameters in Them moi field
    And click Luu button
    And verify popup successful is displayed
    And go back to Dao Tao page
    Then verify all parameters is displayed

