import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from utilities.readProperties import ReadConfig
from pageObjects.ultimateqaUI import ultimateqa

from utilities import XLUtils
path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "TestData",
    "title_testdata.xlsx"
)

class Test_UltimateQA():
    url=ReadConfig.geturl()  #static method can be accessed using class name

    @pytest.mark.sanity
    def test_001_ultimateqa(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        ultimate=ultimateqa(self.driver)
        ultimate.clicklink_findele()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Click button using ClassName']"))
        )
        data={}
        data=XLUtils.exceldatatodict(path, "Sheet1")
        print(data)
        print(self.driver.title)
        print(data["findele"])
        assert self.driver.title==data["findele"]
        ultimate.clicklink_idlink()
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"//*[text()='Button success']"))
        )
        assert self.driver.title==data["idlnk"]
        self.driver.back()  #to navigate back to simple html elements page
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Click button using ClassName']"))
        )
        assert self.driver.title==data["findele"]
        ultimate.clicklink_lnktxt()
        tit=self.driver.find_element(By.XPATH, ultimate.txt_msg_xpath).text
        assert tit==data["msgtitle"]
        self.driver.close()


