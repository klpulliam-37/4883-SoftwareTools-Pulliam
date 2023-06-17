from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.wunderground.com/history/daily/KCHO/date/2020-12-31")

title = driver.title
# assert title == "Web form"

driver.implicitly_wait(5)

observations = driver.find_element(by=By.CSS_SELECTOR, value="lib-city-history-observation")

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

message = driver.find_element(by=By.ID, value="message")
value = message.text
# assert value == "Received!"

driver.quit()