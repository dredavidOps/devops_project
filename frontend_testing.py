from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(""))

element = driver.find_element(By.ID, "user_id")
driver.get("http://127.0.0.1:5001/get_user/2")

# driver.find_element(By.ID, value="user_id")
# driver.find_element(By.CLASS_NAME, value='er8xn').click()
# driver.find_element(By.CLASS_NAME, value='er8xn').send_keys("hello")
# driver.find_element(By.CLASS_NAME, value='er8xn').send()
# user_id = driver.find_element(By.ID, "user_id")
driver.implicitly_wait(100)

print(element)
# print(driver.title)