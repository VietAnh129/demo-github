Feature: Verify Nhan Su page

    Background: Login
        Given Login success with user "ec00003" and pwd "123456789"
        When Click Nhan su field
        And Click Ho so nhan su field
        And Click Nhan vien moi
    @3
    Scenario: Verify auto fill UserID
        Then Verify auto fill UserID "1906"

    @4
    Scenario: Verify auto capitalize first letter
        When input "le viet anh" in Họ và Tên field
        Then verify auto capitalize first letter "Le Viet Anh"

    @5
    Scenario: Verify drop list Gioi Tinh
        When click Giới tính field
        Then verify drop list Gioi Tinh "Nam,Nữ,Khác"

    @6
    Scenario: Verify drop list Hoc Van
        When click Hoc Van field
        Then verify drop list Hoc Van "Cao đẳng,Đại học,LDPT,Sơ cấp,Trung cấp,Thạc sỹ,Tiến sỹ"



