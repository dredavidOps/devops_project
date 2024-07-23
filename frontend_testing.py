import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(""))

driver.get("http://127.0.0.1:5001/get_user/9")

my_data = driver.find_element(By.ID, value="result")
# driver.find_element(By.CLASS_NAME, value='er8xn').click()
# driver.find_element(By.CLASS_NAME, value='er8xn').send_keys("hello")
# driver.find_element(By.CLASS_NAME, value="blockInner")
# driver.find_element(By.ID, "user_id")

print(my_data)
time.sleep(100)