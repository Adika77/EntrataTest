from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from assertpy import assert_that

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.entrata.com/")
driver.maximize_window()

resource = driver.find_element(By.XPATH,"(//a[@href='/resources'])[1]")
resource.click()

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

heading = driver.find_element(By.XPATH,"//h2").text

assert_that(heading).contains("Resource")