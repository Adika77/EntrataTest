from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.entrata.com/")  # opens URL
driver.maximize_window()                # maximize browser window

watchDemo = driver.find_element(By.LINK_TEXT,"Watch Demo")
watchDemo.click()                       # clicks on watchdemo button

firstName = driver.find_element(By.XPATH,"//input[@id='FirstName']")
firstName.send_keys("Entrata")

lastName = driver.find_element(By.XPATH,"//input[@id='LastName']")
lastName.send_keys("India")

email = driver.find_element(By.XPATH,"//input[@id='Email']")
email.send_keys("abc@gmail.com")

companyName = driver.find_element(By.XPATH,"//input[@id='Company']")
companyName.send_keys("abc@gmail.com")

PhoneNumber = driver.find_element(By.XPATH,"//input[@id='Phone']")
PhoneNumber.send_keys("1234567891")

unitCount = Select(driver.find_element(By.TAG_NAME,"select"))
unitCount.select_by_index(1)

jobTitle = driver.find_element(By.XPATH,"//input[@id='Title']")
jobTitle.send_keys("Software Test Engineer")

heading = driver.find_element(By.ID,"Banner_Title").text

assert_that(heading).contains("Optimize")
