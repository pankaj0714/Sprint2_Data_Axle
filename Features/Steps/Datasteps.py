from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    context.driver.maximize_window()


@when('open DataAxel Login')
def openLogin(context):
    context.driver.get("https://www.dataaxlegenie.com")

    #print(driver.title)
    #print(driver.current_url)
    context.driver.get("https://www.dataaxlegenie.com")

@then('verify that the user login on page')
def verifyLogin(context):
    context.driver.get("https://auth.salesgenie.com/account/mixed?ReturnUrl=%2fissue%2fwsfed%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fapp.salesgenie.com%26wctx%3drm%253d0%2526id%253dpassive%2526ru%253d%25252fHome%25252fHome%25252f%26wct%3d2021-06-28T16%253a41%253a10Z%26wreply%3dhttps%253a%252f%252fapp.salesgenie.com%252fHome%252fHome&wa=wsignin1.0&wtrealm=https%3a%2f%2fapp.salesgenie.com&wctx=rm%3d0%26id%3dpassive%26ru%3d%252fHome%252fHome%252f&wct=2021-06-28T16%3a41%3a10Z&wreply=https%3a%2f%2fapp.salesgenie.com%2fHome%2fHome")
    context.driver.find_element_by_id("formSignIn").click()
    context.driver.get("https://auth.salesgenie.com/account/mixed?ReturnUrl=%2fissue%2fwsfed%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fapp.salesgenie.com%26wctx%3drm%253d0%2526id%253dpassive%2526ru%253d%25252fHome%25252fHome%25252f%26wct%3d2021-06-28T16%253a41%253a10Z%26wreply%3dhttps%253a%252f%252fapp.salesgenie.com%252fHome%252fHome&wa=wsignin1.0&wtrealm=https%3a%2f%2fapp.salesgenie.com&wctx=rm%3d0%26id%3dpassive%26ru%3d%252fHome%252fHome%252f&wct=2021-06-28T16%3a41%3a10Z&wreply=https%3a%2f%2fapp.salesgenie.com%2fHome%2fHome")
    context.driver.find_element_by_id("UserName").send_keys("hh")
    context.driver.find_element_by_id("formSignIn").click()
    context.driver.get("https://auth.salesgenie.com/account/mixed?ReturnUrl=%2fissue%2fwsfed%3fwa%3dwsignin1.0%26wtrealm%3dhttps%253a%252f%252fapp.salesgenie.com%26wctx%3drm%253d0%2526id%253dpassive%2526ru%253d%25252fHome%25252fHome%25252f%26wct%3d2021-06-28T16%253a41%253a10Z%26wreply%3dhttps%253a%252f%252fapp.salesgenie.com%252fHome%252fHome&wa=wsignin1.0&wtrealm=https%3a%2f%2fapp.salesgenie.com&wctx=rm%3d0%26id%3dpassive%26ru%3d%252fHome%252fHome%252f&wct=2021-06-28T16%3a41%3a10Z&wreply=https%3a%2f%2fapp.salesgenie.com%2fHome%2fHome")
    context.driver.find_element_by_id("UserName").send_keys("Pankaj.Rajwaniya@data-axle.com")
    context.driver.find_element_by_id("Password").send_keys("Kipl@123")
    context.driver.find_element_by_id("formSignIn").click()
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.driver.get_screenshot_as_file("screen.png")
   # assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()
