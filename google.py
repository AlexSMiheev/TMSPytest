import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


def test_google(get_driver):
    chrome = get_driver
    url = 'http://google.com/'
    chrome.get(url=url)
    chrome.maximize_window()
    search_box = chrome.find_element(By.NAME, 'q')
    search_box.send_keys('python 3.10')
    search_box.submit()
    assert 'python 3.10' in chrome.title
