Feature: Verify Dien Thoai

    Background: Login
      Given login success with user "ec00003" and pwd "123456789"
        When click Nhan su field
        And click Ho so nhan su field
        And click Nhan vien moi

  @7
    Scenario Outline: Input phone number does not start from 0
      When input phone number '<phone>' in phone number field
      And click Tab
      Then verify error "Số điện thoại sai định dạng" is displayed
    Examples:
        |phone|
        |987654321|
        |   0123  |
        |  012345678901   |
        |   0987@12349    |
        |   0987654321    |


