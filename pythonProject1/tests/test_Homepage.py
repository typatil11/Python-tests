import time
from telnetlib import EC

import requests
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from utilities import HomepageData
from utilities.BaseClass import BaseClass
from utilities.HomePage import HomePage
import pytest


class TestHomepage(BaseClass):

    def test_formSubmission(self,getData):


        homepage=HomePage(self.driver)
        time.sleep(3)
        homepage.getName().send_keys(getData["FirstName"])
        homepage.getEmail().send_keys(getData["LastName"])
        self.selectOptionBytext(homepage.getGender(),getData["Gender"])

        homepage.getSubmit().click()
        alertText =homepage.getSuccesText().text

        assert ("success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.test_HomePage_Data)
    def getData(self,request):
        return request.param







