
class RegistrationLocators:

    FIRST_NAME_FIELD_LOC = ('css selector', "input[id='name']")
    LAST_NAME_FIELD_LOC = ("css selector", "input[id='surname']")
    EMAIL_FIELD_LOC = ("css selector", "input[id='email']")
    PASSWORD_FIELD_LOC = ("css selector", "input[id=password']")
    REPEAT_PASSWORD_FIElD_LOC = ("css selector", "input[id='password_repeat']")
    REGISTER_BTN = ("xpath", "//button[text()='Зарегистрироваться']")
    SUCCESS_MESSAGE_LOC = ("xpath", "//div[contains(@class, 'h3')]")



