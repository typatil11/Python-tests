from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def verify_title():
    msg = "test"
    assert msg == "test"


def test_program():
    msg = "hello"
    assert msg == "hello"

print("Tets");