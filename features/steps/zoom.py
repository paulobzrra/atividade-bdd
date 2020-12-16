from lib2to3.pgen2 import driver

import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)

from main_functions import *

use_step_matcher("re")

@given("platform site is running")
def step_impl(context):
    options = Options()
    options.add_argument('--incognito')
    options.add_argument("window-size=1400,800")
    context.driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'driver', 'chromedriver.exe'), options=options)
    context.driver.get('https://homologacao.leadfortaleza.com.br/ead/login')
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'logo-dell')))

    username = context.driver.find_element_by_id('login')
    username.send_keys('pauloalunoteste')

    password = context.driver.find_element_by_id('password')
    password.send_keys('abcd1234')

    login_button = context.driver.find_element_by_id('login-btn')
    login_button.click()
    time.sleep(2)

@when("the user select increase font size in acessibility menu")
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'smallHeader')))
    my_courses = context.driver.find_element_by_id('smallHeader').text
    assert my_courses == "My Courses"

    time.sleep(2)

    btn_fontIncrease = context.driver.find_element_by_id('btFontIncrease')
    btn_fontIncrease.click()

    time.sleep(3)

@then("the letters in the screen grow up")
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID,'smallHeader')))
    fontsize = context.driver.find_element_by_id('smallHeader').value_of_css_property("font-size")
    assert fontsize == "30.6px"



