from selenium.webdriver.common.by import By


class Login:
    textbox_username_id="Email"  # type of element_what element_what type of xpath we are taking here
    textbox_password_id="Password"
    button_login_xpath="//button[@type='submit']"
    link_logout_linktext="Logout"

    def __init__(self, driver):
        self.driver=driver

    def set_UserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_Password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_linktext).click()


