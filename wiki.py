from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome()
    url = 'https://ru.wikipedia.org/'
    chrome.get(url=url)
    chrome.maximize_window()
    search_box = chrome.find_element(By.CLASS_NAME, 'vector-search-box-input')
    search_box.send_keys('Автоматизация')
    search_box.submit()
    assert 'Автоматизация' in chrome.title
    chrome.close()
