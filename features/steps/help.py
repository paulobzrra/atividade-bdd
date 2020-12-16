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

@given("platform is running")
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


@when("the user select help")
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID, 'smallHeader')))
    my_courses = context.driver.find_element_by_id('smallHeader').text
    assert my_courses == "My Courses"

    btn_help = context.driver.find_element_by_id('bt-help')
    btn_help.click()

    time.sleep(3)


@then("platform shows the help center")
def step_impl(context):
    WebDriverWait(context.driver, 3).until(EC.visibility_of_element_located((By.ID,'smallHeader')))
    small_header = context.driver.find_element_by_id('smallHeader').text
    assert small_header == "Help Center"