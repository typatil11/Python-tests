import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.keys import Keys
import time

from utilities.BaseClass import BaseClass
from utilities.CheckoutPage import CheckoutPage
from utilities.HomePage import HomePage


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log=self.getLogger()


        homepage = HomePage(self.driver)
        checkoutpage= homepage.shopItems()
        log.info("Getting all card titles")
        cards= checkoutpage.getCardTitles()

        i = -1
        for card in cards:
            i= i + 1
            cardText=card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getName()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutpage.CheckoutItems()
        log.info("Entering Country Name")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.VerifyLink("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text recieved from application is "+success_text)
        assert "Success! ThankDS you!" in success_text
        self.driver.close()

