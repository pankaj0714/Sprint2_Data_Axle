import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import os
#b = int(input())
b = 2
print(b)

@given('launch Admin in Multi browser')
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


@when('open sprint2 DataAxel Admin')
def openLoginsprint1(context):
    context.driver.get("https://test-admin.dataaxlegenie.com")
    #context.driver.get("https://dev-app.dataaxlegenie.com/audience#n/0/")
    time.sleep(5)
    # context.driver.find_element_by_id("details-button").click()
    # time.sleep(5)
    # context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(5)
    # context.driver.find_element_by_id("proceed-link").click()
    # time.sleep(5)

@then('verify Admin that the user signinsearch on page')
def verifyLoginsprint1(context):
    context.driver.find_element_by_xpath("//input[@id='UserName']").send_keys("Pankaj.Rajwaniya@data-axle.com.test")
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@id='Password']").send_keys("Kipl@123")
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='Sign In']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='Continue']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//a[normalize-space()='Users']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@id='keywords']").send_keys("Pankaj.Rajwaniya@data-axle.com.test")
    time.sleep(5)
    context.driver.find_element_by_xpath("//button[normalize-space()='Search']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='Pankaj.Rajwaniya@data-axle.com']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//a[normalize-space()='US Consumer']").click()
    time.sleep(5)
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    context.driver.find_element_by_xpath("//body/div[@id='wrap']/div[2]/div[1]/div[3]/div[1]/section[22]/div[2]/ul[1]/li[2]/a[1]").click()
    time.sleep(5)
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='Personal Info']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='Personal Info']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='B2C Link']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//span[normalize-space()='Birth Month']").click()
    time.sleep(5)
    context.driver.find_element_by_xpath("//a[normalize-space()='Log Out']").click()
    time.sleep(5)
    context.driver.get_screenshot_as_file("screen.png")
    time.sleep(5)
    #web
    context.driver.get("https://test-app.salesgenie.com/audience#n/0/")
    context.driver.implicitly_wait(100)
    # context.driver.find_element_by_xpath("//div[normalize-space()='Search verified U.S. businesses']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[@class='filter-database-popup__overlay filter-database-popup__overlay--show']").click()
    context.driver.implicitly_wait(100)
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
    context.driver.find_element_by_xpath("//body[1]/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/section[2]/div[1]/div[1]/div[2]/div[3]/div[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/ul[2]/li[4]/i[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//a[normalize-space()='Sign Out']").click()
    time.sleep(10)

@then('Admin close browser')
def closeBrowsersprint1(context):
    #context.sleep(6000)
    context.driver.close()
