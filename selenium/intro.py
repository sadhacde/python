from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

URL = "https://www.amazon.com/Roche-Posay-Toleriane-Double-Repair-Moisturizer/dp/B01N9SPQHQ/ref=sr_1_5?crid=120R1YXMYSYUU&dib=eyJ2IjoiMSJ9.jpf_J3GYyuxxDEHy1BxJOJUkJ-xvnV2ESvodazDoFJ83CHfdjqIizCjlwXurbxcxo-qHaOXaAguCMOpGJ63yJxbZVhf04PSrqP2GYHTBjMkwLgqWKcBH5EEIF6jC4WSVJyB2vWWBzjbJYgaWyON65WMhZm2hldns5p1hwj-nEx8tbsGl_xvHhcWho45vUC7Oz5dDUUpdr0icJX6TgYgo4adsSVYCtn1Oh_Pkp2NDs6V0ur2Rf-p7-zHb8lfAgkUKHwTeOL89e_zEYhdRXszj2_7K8lwsqedrRyF__tkr8_A._TV8qOvBD15sfStR_BfEmx4UbHOQ3olx4N_jfDY01NA&dib_tag=se&keywords=moisturizer&qid=1727994301&sprefix=moisturize%2Caps%2C100&sr=8-5"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, "submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# dbug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(dbug_link.text)

names = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")
names = [n.text for n in names]
names.remove("More")

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
times = [datetime.fromisoformat(t.get_attribute("datetime")).strftime("%Y-%m-%d") for t in times]

upcoming_events = {i:{"time": times[i], "name": names[i]} for i in range(len(names))}
print(upcoming_events)

driver.quit()
