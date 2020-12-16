import time
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_spinner(driver):
    while True:
        if not driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed():
            break

def wait_alert():
    # sec = randint(4)
    time.sleep(4)

def wait_sec():
    sec = randint(15, 20)
    time.sleep(sec)

# def wait_alert(driver):
#     while True:
#         if not driver.find_element_by_class_name('fadeIn alert-success').is_displayed():
#             break

def login(username, password, driver):


    create_minicompany = EC.presence_of_element_located(
        (By.XPATH,
         '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[1]/div/a'))
    WebDriverWait(driver, 15).until(create_minicompany)


def monitor_minicompany(driver):
    name_field = driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-companies/div/div[1]/table/tbody/tr/td[1]/input')
    name_field.send_keys('Automated Test - Mini Company')

    wait_spinner(driver)

    search_button = driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-companies/div/div[2]/app-filter-actions/div/button[2]')
    search_button.click()

    monitor_button_wait = EC.element_to_be_clickable(
        (By.XPATH,
         '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/a'))
    WebDriverWait(driver, 15).until(monitor_button_wait)

    monitor_button = driver.find_element_by_xpath(
        '/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/a')
    monitor_button.click()