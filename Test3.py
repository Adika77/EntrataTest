from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.entrata.com/")
driver.maximize_window()

a = ActionChains(driver)
m= driver.find_element(By.XPATH,"(//div[@class='main-nav-link'])[2]")
a.move_to_element(m).perform()

element = WebDriverWait(driver, 11).until(
EC.presence_of_element_located((By.XPATH,"(//a[@href='/military'])[1]")))
element.click()

n = driver.find_element(By.XPATH,"(//a[@href='/military'])[1]")
a.move_to_element(n).click().perform()


title = driver.title

assert_that(title).contains("Military ")