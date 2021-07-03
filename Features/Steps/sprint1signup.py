import time

from behave import *
from selenium import webdriver
from time import sleep

@given('launch sprint1 signup chrome browser')
def launchsignupsprint1(context):
    context.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    context.driver.maximize_window()


@when('open sprint1 signup DataAxel Login')
def opensignupsprint1(context):
    context.driver.get("https://test-app.salesgenie.com/audience#n/0/")
    context.driver.find_element_by_xpath("//div[@class='filter-database-popup__overlay filter-database-popup__overlay--show']").click()
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_id("thin-search-register").click()

@then('verify sprint1 that the user signup on page')
def verifysignupsprint1(context):
    # case1
    context.driver.find_element_by_xpath("//input[@name='name']").clear()
    context.driver.find_element_by_xpath("//input[@name='name']").send_keys("karan")
    context.driver.find_element_by_xpath("//input[@name='companyName']").clear()
    context.driver.find_element_by_xpath("//input[@name='companyName']").send_keys("paul pvt ltd")
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("paul@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//input[@name='phone']").clear()
    context.driver.find_element_by_xpath("//input[@name='phone']").send_keys("248-909-8999")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    context.driver.find_element_by_xpath("//button[normalize-space()='Get Started']").click()
    time.sleep(10)
    # case2
    context.driver.find_element_by_xpath("//input[@name='name']").clear()
    context.driver.find_element_by_xpath("//input[@name='name']").send_keys("lamp singh")
    context.driver.find_element_by_xpath("//input[@name='companyName']").clear()
    context.driver.find_element_by_xpath("//input[@name='companyName']").send_keys("paul pvt ltd")
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("ryan")
    context.driver.find_element_by_xpath("//input[@name='phone']").clear()
    context.driver.find_element_by_xpath("//input[@name='phone']").send_keys("8824510655")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    context.driver.find_element_by_xpath("//button[normalize-space()='Get Started']").click()
    time.sleep(10)
    # case3
    context.driver.find_element_by_xpath("//input[@name='name']").clear()
    context.driver.find_element_by_xpath("//input[@name='name']").send_keys("ramp singh")
    context.driver.find_element_by_xpath("//input[@name='companyName']").clear()
    context.driver.find_element_by_xpath("//input[@name='companyName']").send_keys("paul pvt ltd")
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("paul@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//input[@name='phone']").clear()
    context.driver.find_element_by_xpath("//input[@name='phone']").send_keys("248-252-8999")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("1234567")
    context.driver.find_element_by_xpath("//button[normalize-space()='Get Started']").click()
    time.sleep(10)
    # case4
    context.driver.find_element_by_xpath("//input[@name='name']").clear()
    context.driver.find_element_by_xpath("//input[@name='name']").send_keys("paul singh")
    context.driver.find_element_by_xpath("//input[@name='companyName']").clear()
    context.driver.find_element_by_xpath("//input[@name='companyName']").send_keys("paul pvt ltd")
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("paul@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//input[@name='phone']").clear()
    context.driver.find_element_by_xpath("//input[@name='phone']").send_keys("248-444-8999")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    context.driver.find_element_by_xpath("//button[normalize-space()='Get Started']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//ul[@class='margin-top__1']/li[3]").click()
    context.driver.find_element_by_xpath("//button[normalize-space()='Get Code']").click()
    context.driver.find_element_by_xpath("//input[@name='verificationCode']").send_keys("123456")
    context.driver.find_element_by_xpath("//button[normalize-space()='Verify']").click()
    context.driver.get_screenshot_as_file("screen.png")

@then('sprint1signup close browser')
def closeBrowsersprint1(context):
    context.sleep(10)
    context.driver.close()
