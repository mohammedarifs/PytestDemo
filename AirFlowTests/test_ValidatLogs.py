import time
from lib2to3.pgen2.driver import Driver
from xml.etree.ElementPath import xpath_tokenizer

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import *
# from conftest import *
# driver=None
#
# @pytest.fixture()
# def initiate_driver():
#      global driver
#      driver = webdriver.Chrome()

def test_validate_airflow_logs(initiate_driver):
    #Initializing driver
    # driver = webdriver.Chrome()
    #lauching browser
    print(initiate_driver)
    driver=initiate_driver
    driver.get("C:\\Users\mohshaik13\Desktop\index.html")
    #checking status for job
    statusField=driver.find_element(By.XPATH,'//button["Hover to view status"]')
    actions = ActionChains(driver)
    actions.move_to_element(statusField).perform()
    time.sleep(1)
    status=statusField.get_attribute('title')
    print("job status", status)
    #validating job status
    assert status == "Success" , "Logs validation failed"
    #opening job window
    driver.find_element(By.XPATH,'//a[contains(text(),"View the jobs on Airflow")]').click()
    time.sleep(1)
    #switching to child window
    parentwindow=driver.current_window_handle
    windows=driver.window_handles
    for window in windows:
        if(window!=parentwindow):
            driver.switch_to.window(window)
            time.sleep(1)
            #opening logs
            driver.find_element(By.XPATH, '//button[contains(text(),"Click to view logs")]').click()
            time.sleep(1)
            #reading logs
            txt=driver.find_element(By.XPATH, '//div').text
            #closing child window
            driver.close()
            #storing logs data in logsfile
            with open(".//logsfile.txt", "w") as file:
                file.write(txt)
                file.close()
            #Valiting logs content and success message
            if "generating secret for digest authentication" in txt:
                assert True
                print("-- validation pass  --")
            else:
                assert  False,"validation failed"

    driver.quit()
    print("completed")
