import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']").click()
time.sleep(2)
driver.find_element(By.NAME, 'username').send_keys('999')
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys('1234')
driver.find_element(By.NAME, 'signon').click()
time.sleep(2)
driver.find_element(By.XPATH, "//img[@src='../images/sm_dogs.gif']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='K9-RT-01']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Add to Cart']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to Checkout']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='newOrder']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Confirm']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Return to Main Menu']").click()