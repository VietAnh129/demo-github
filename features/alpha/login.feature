Feature: Login page
  @1
  Scenario: Login page successfully
    Given Open page
    When Input username "EC00003" and password "123456789"
    And Click login button
    Then Verify login successfully title "Bảng tin"
  @2
  Scenario: Login page failed`
    Given Open page
    When Input username "admin" and password "123456789"
    And Click login button
    Then Verify error message "ID nhân viên hoặc mật khẩu không hợp lệ"