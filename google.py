from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google():
    chrome = webdriver.Chrome()
    url = 'http://google.com/'
    chrome.get(url=url)
    chrome.maximize_window()
    search_box = chrome.find_element(By.NAME, 'q')
    search_box.send_keys('python 3.10')
    search_box.submit()
    assert 'python 3.10' in chrome.title
    chrome.close()
