import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*******************Test_001_Login**************************")
        self.logger.info("*******************Verifying Home Page Title**************************")
        driver=setup
        driver.get(self.baseURL)
        act_title=driver.title
        if act_title=="nopCommerce demo store. Login":
            assert True
            driver.close()
            self.logger.info("*******************home page title passed **************************")
        else:
            driver.save_screenshot(".//Screenshots/"+"test_homePageTitle.png")
            driver.close()
            self.logger.error("*******************home page title failed**************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*******************verifying login test**************************")
        driver=setup
        driver.get(self.baseURL)
        lp=Login(driver)
        lp.set_UserName(self.username)
        lp.set_Password(self.password)
        lp.clickLogin()
        time.sleep(2)
        act_title=driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******************login test passed**************************")
            driver.close()
        else:
            driver.save_screenshot(".//Screenshots/" + "test_login.png")
            self.logger.error("******************* login failed**************************")
            driver.close()
            assert False


