import time

from behave import *
from selenium import webdriver
from time import sleep

@given('launch sprint1 forgot chrome browser')
def launchBrowsersprint1(context):
    context.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    context.driver.maximize_window()


@when('open sprint1 DataAxel forgot')
def openforgotsprint1(context):
    context.driver.get("https://test-app.salesgenie.com/audience#n/0/")
    context.driver.find_element_by_xpath("//div[@class='filter-database-popup__overlay filter-database-popup__overlay--show']").click()
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_id("thin-search-signin").click()
    forgetEmail = context.driver.find_element_by_xpath("//a[normalize-space()='Forgot your Password?']")
    context.driver.execute_script("arguments[0].click();", forgetEmail)
    #context.driver.find_element_by_xpath("//a[normalize-space()='Forgot your Password?']").click()


@then('verify sprint1 that the user forgot on page')
def verifyforgotsprint1(context):
    # case 1
    context.driver.find_element_by_xpath("//input[@name='email']").click()
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("jack11")
    context.driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
    time.sleep(10)
    # case 2
    # driver.find_element_by_xpath("//input[@name='email']").click()
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("rock@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
    time.sleep(10)
    # case 3
    context.driver.find_element_by_xpath("//input[@name='email']").clear()
    context.driver.find_element_by_xpath("//input[@name='email']").send_keys("jack11@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//button[normalize-space()='Submit']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//ul[@class='margin-top__1']/li[3]").click()
    context.driver.find_element_by_xpath("//button[normalize-space()='Get Code']").click()
    context.driver.find_element_by_xpath("//input[@name='verificationCode']").send_keys("123456")
    context.driver.find_element_by_xpath("//button[normalize-space()='Verify']").click()
    #context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    #context.driver.find_element_by_xpath("//button[normalize-space()='Create Password']").click()
    context.driver.get_screenshot_as_file("screen.png")

@then('sprint1forgot close browser')
def closeBrowsersprint1(context):
    context.sleep(10)
    context.driver.close()
