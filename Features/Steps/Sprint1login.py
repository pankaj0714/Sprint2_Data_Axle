import time
from behave import *
from selenium import webdriver

@given('launch sprint1 chrome browser')
def launchBrowsersprint1(context):
    context.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    context.driver.maximize_window()


@when('open sprint1 DataAxel signin')
def openLoginsprint1(context):
    context.driver.get("https://test-app.salesgenie.com/audience#n/0/")
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath("//div[@class='filter-database-popup__overlay filter-database-popup__overlay--show']").click()
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_id("thin-search-signin").click()
    #context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()

@then('verify sprint1 that the user signin on page')
def verifyLoginsprint1(context):
    #case 0
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(10)
    # case 1
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("harsh11")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(10)
    # case 2
    #context.driver.find_element_by_xpath("//input[@type='text']").clear()
    #context.driver.find_element_by_xpath("//input[@type='text']").send_keys("tan11@yopmail.com")
    #context.driver.find_element_by_xpath("//input[@type='password']").clear()
    #context.context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    #time.sleep(10)
    #context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    #time.sleep(10)
    # case 3
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("harsh11@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    time.sleep(10)
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(10)
    context.driver.get_screenshot_as_file("screen.png")

@then('sprint1login close browser')
def closeBrowsersprint1(context):
    context.sleep(10)
    context.driver.close()
