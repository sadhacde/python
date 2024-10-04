from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Name")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Name2")

email = driver.find_element(By.NAME, "email")
email.send_keys("atest@gmail.com")

button = driver.find_element(By.TAG_NAME, 'button')
button.click()
