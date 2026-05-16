from selenium.webdriver.common.by import By


class ultimateqa:
    lnk_findele_xpath="//a[text()='Interactions with simple elements']"
    lnk_idexample_id="idExample"
    lnk_link_lnktext="Click me using this link text!"
    txt_msg_xpath="//*[text()='Link success']"

    def __init__(self, driver):
        self.driver=driver
    def clicklink_findele(self):
        self.driver.find_element(By.XPATH, self.lnk_findele_xpath).click()
    def clicklink_idlink(self):
        self.driver.find_element(By.ID, self.lnk_idexample_id).click()
    def clicklink_lnktxt(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_link_lnktext).click()



