import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import os
#b = int(input())
from selenium.webdriver.support.select import Select

b = 2
print(b)

@given('launch Multi browser search')
def launchBrowsersprintsearchlogin(context):
    path = str(os.getcwd())
    if b==1:
        context.driver = webdriver.Firefox(executable_path=path + "\geckodriver.exe")
        context.driver.maximize_window()
    elif b==2:
        context.driver = webdriver.Edge(executable_path=path + "\msedgedriver.exe")
        context.driver.maximize_window()
    elif b==3:
        context.driver = webdriver.Opera(executable_path=path + "\operadriver.exe")
        context.driver.maximize_window()
    elif b==4:
        context.driver = webdriver.Chrome(executable_path=path + "\chromedriver.exe")
        context.driver.maximize_window()


@when('open sprint2 DataAxel search')
def openLoginsearch(context):
    context.driver.get("https://test-app.salesgenie.com/audience#n/0/")
    context.driver.implicitly_wait(100)
    # context.driver.find_element_by_xpath("//div[normalize-space()='Search verified U.S. businesses']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[@class='filter-database-popup__overlay filter-database-popup__overlay--show']").click()
    context.driver.implicitly_wait(100)

@then('verify Movetooltip that the user search on page')
def verifyLoginsearch(context):
    context.driver.find_element_by_id("thin-search-signin").click()
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("Pankaj.Rajwaniya@data-axle.com.test")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    time.sleep(10)
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/main[1]/section[1]/nav[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/main[1]/section[1]/nav[1]/div[2]/div[3]/div[1]/div[1]/img[1]").click()
    time.sleep(10)
    # Personal Info
    context.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("b")
    time.sleep(10)
    context.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("a")
    context.driver.find_element_by_xpath("//input[@placeholder='First Name']").click()
    time.sleep(10)
    select = Select(context.driver.find_element_by_xpath("//select[@name='range']"))
    select.select_by_value("CA")
    time.sleep(10)
    # context.driver.find_element_by_xpath("//input[@placeholder='All']").send_keys("a")
    # time.sleep(10)
    # context.driver.find_element_by_xpath("//input[@placeholder='Number and/or street name']").send_keys("Goyal")
    # time.sleep(10)
    # context.driver.find_element_by_xpath("//input[@placeholder='Enter a ZIP Code']").send_keys("Goyal")
    # time.sleep(10)
    context.driver.find_element_by_xpath("//button[normalize-space()='Run Search']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/ul[2]/li[4]/i[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//a[normalize-space()='Sign Out']").click()
    time.sleep(10)

@then('search close browser')
def closeBrowsersearch(context):
    #context.sleep(6000)
    context.driver.close()
