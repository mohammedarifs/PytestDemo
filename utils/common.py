import time
from jproperties import Properties
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = None

def initiate_webdriver():
    global driver
    driver = webdriver.Chrome()
    return driver

def launch_browser(url):
    driver.get(url)

def mouse_hover(locator):
    actions = ActionChains(driver)
    actions.move_to_element(get_locators(locator)).perform()

def time_out(n):
    time.sleep(n)

def get_locators(locator):
    loc=load_locators(locator)
    return driver.find_element(By.XPATH,loc)

def get_attributevalue(loc, atr):
    return get_locators(loc).get_attribute(atr)

def get_current_window():
    return driver.current_window_handle

def get_all_windows():
    return driver.window_handles





def close_all_browser():
    driver.quit()

def load_config(value):
    configs = Properties()
    with open('../config/config.properties', 'rb') as read_prop:
        configs.load(read_prop)
    return configs.get(value).data

def load_locators(value):
    configs = Properties()
    with open('../config/locators.properties', 'rb') as read_prop:
        configs.load(read_prop)
    return configs.get(value).data

def switch_to_child_window(parentwindow):
    for window in get_all_windows():
        if(window!=parentwindow):
            driver.switch_to.window(window)

def switch_to_window(window):
    driver.switch_to.window(window)

def click_btn(btn):
    get_locators(btn).click()

def get_text(locator):
    return get_locators(locator).text

def close_browser():
    driver.close()
