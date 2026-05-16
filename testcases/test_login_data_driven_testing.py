import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils

class Test_002_Login_DDT:
    baseURL= ReadConfig.getApplicationURL()
    path=".//python_selenium_pytest/TestData/testdata_python_selenium_pytest.xlsx"


    logger=LogGen.loggen()
    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("*******************Test_002_Login_DDT**************************")
        self.logger.info("*******************verifying login test data driven testing**************************")
        driver=setup
        driver.get(self.baseURL)
        lst=[]
        lp=Login(driver)
        rowcount=XLUtils.getRowCount(self.path, 'Sheet1')
        for r in range(2, rowcount+1):
            user=XLUtils.readData(self.path,'Sheet1', r, 1)
            password=XLUtils.readData(self.path,'Sheet1', r, 2)
            exp_result=XLUtils.readData(self.path,'Sheet1', r, 3)

            lp.set_UserName(user)
            lp.set_Password(password)
            lp.clickLogin()
            time.sleep(2)
            act_title=driver.title
            if act_title=="Dashboard / nopCommerce administration":
                if exp_result=="Pass":
                    self.logger.info("***passed****")
                    lp.clickLogout()
                    lst.append("pass")
                elif exp_result=="Fail":
                    self.logger.info("***failed****")
                    lp.clickLogout()
                    lst.append("fail")
            elif act_title!="Dashboard / nopCommerce administration":
                if exp_result=="Pass":
                    self.logger.info("***failed****")
                    lst.append("fail")
                    lp.clickLogout()
                elif exp_result=="Fail":
                    self.logger.info("***passed****")
                    lst.append("pass")
                    lp.clickLogout()

        if "fail" not in lst:
            self.logger.info("***login DDT test passed***")
            driver.close()
            assert True
        else:
            self.logger.info("***login DDT test failed***")
            driver.close()
            assert False
        self.logger.info("*******************Test_002_Login_DDT completed**************************")



