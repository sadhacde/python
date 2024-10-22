# challenge: automate data entry of rentable places in San Francisco into a google form

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

form = 'Google-Form'
url = 'https://appbrewery.github.io/Zillow-Clone/'
header = {
    "User-Agent": "",
    "Accept-Language": ""
}

response = requests.get(url, headers=header)
zillow = response.text

soup = BeautifulSoup(zillow, "html.parser")

addresses = []
for adr in soup.find_all("address"):
    addresses.append(adr.text.replace('\n', '').replace('|', '').strip())

prices = []
for price in soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine"):
    prices.append(price.text.split()[0][:6].strip())

links =[]
for link in soup.find_all("a", class_="property-card-link"):
    links.append(link.get('href'))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent= ")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):
    driver.get(form)
    time.sleep(2)
    
    adr_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    adr_input.send_keys(addresses[n])
        
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(prices[n])
        
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(links[n])

    button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()