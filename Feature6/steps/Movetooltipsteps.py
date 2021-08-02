import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import os
#b = int(input())
b = 2
print(b)

@given('launch Multi browser')
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


@when('open sprint2 DataAxel Movetooltip')
def openLoginsprint2(context):
    context.driver.get("https://test-app.salesgenie.com/audience#n/0/")
    #context.driver.get("https://dev-app.dataaxlegenie.com/audience#n/0/")
    context.driver.implicitly_wait(100)
    #context.driver.find_element_by_xpath("//div[normalize-space()='Search verified U.S. businesses']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[@class='filter-database-popup__overlay filter-database-popup__overlay--show']").click()
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_id("thin-search-signin").click()
    #context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()

@then('verify Movetooltip that the user signinsearch on page')
def verifyLoginsprint2(context):
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
    context.driver.find_element_by_xpath("//input[@type='text']").clear()
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("Pankaj.Rajwaniya@data-axle.com.test")
    #context.driver.find_element_by_xpath("//input[@type='text']").send_keys("jack11@infogroup.mailinator.com")
    context.driver.find_element_by_xpath("//input[@type='password']").clear()
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys("Kipl@123")
    #context.driver.find_element_by_xpath("//input[@type='password']").send_keys("test123")
    time.sleep(10)
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/main[1]/section[1]/nav[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/main[1]/section[1]/nav[1]/div[2]/div[3]/div[1]/div[1]/img[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[contains(@class,'filter-item')][normalize-space()='Name']").click()
    time.sleep(10)
    a = ActionChains(context.driver)
    m = context.driver.find_element_by_xpath("//body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/section[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]")
    a.move_to_element(m).perform()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[contains(@class,'filter-item')][normalize-space()='Name']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[@data-auto='Age']//input[@type='checkbox']").click()
    time.sleep(10)
    c = ActionChains(context.driver)
    d = context.driver.find_element_by_xpath("//body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/section[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]")
    c.move_to_element(d).perform()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[@data-auto='Age']//input[@type='checkbox']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//div[@data-auto='Gender']//input[@type='checkbox']").click()
    time.sleep(10)
    c = ActionChains(context.driver)
    d = context.driver.find_element_by_xpath("//body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/section[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/i[1]")
    c.move_to_element(d).perform()
    time.sleep(10)
    context.driver.find_element_by_xpath("//input[@value='M']").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//input[@value='F']").click()
    time.sleep(10)
    # Personal Info
    context.driver.find_element_by_xpath("//body/div[1]/div[4]/div[1]/div[3]/div[1]/div[2]/section[2]/div[1]/div[1]/div[2]/div[3]/div[1]").click()
    time.sleep(10)
    context.driver.execute_script("window.scroll(0, 0);")
    time.sleep(5)
    context.driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/ul[2]/li[4]/i[1]").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("//a[normalize-space()='Sign Out']").click()
    time.sleep(10)


@then('Movetooltip close browser')
def closeBrowsersprint1(context):
    #context.sleep(6000)
    context.driver.close()
