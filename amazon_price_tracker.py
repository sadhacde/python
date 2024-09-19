'''
scrapes price of an item from amazon. when run, checks if current price is below desired buy price
great for black friday season!
'''

from bs4 import BeautifulSoup
import requests
import smtplib

import os

url= "https://www.amazon.com/Roche-Posay-Toleriane-Double-Repair-Moisturizer/dp/B01N9SPQHQ/ref=sr_1_1?dib=eyJ2IjoiMSJ9.nnNB8BwjB2cid_Anzc0NHddlTkPEh1mmSMn8Ym6uJktFuUJgfdkszSx8e36aegRTNDIwrHJeqAjhbcU1jVal-TelfoCVRFebDwoLphqv6QTc5wUQLX_bRls2raGBOL2WOZQbo9z5H75Qar5BDi1zjiHTSn_2zTOYOtJ5V2P7XG65lkNk8aA9FYQ9hRFRYj2qNKyhV9JBne7g7pJFUL4k-KEmVkoiKDRllbS7NK_KKyDPGNEHRyxlG2Y1D552MWBMJWv4gIUm9XUcZXKhT1D780oQcqgO_1fXKUOSTL1EH5o.o3-dt-ZuE9VHvjuFm3IYGXtYSQB_1Rr2Jj6XO1WxxPM&dib_tag=se&hvadid=697549558517&hvdev=c&hvlocphy=9026804&hvnetw=g&hvqmt=b&hvrand=8062968110715955306&hvtargid=kwd-960425568615&hydadcr=27504_14522349&keywords=la+roche+posay+double+moisturizer&qid=1726757944&sr=8-1"

response = requests.get(url)
moisturizer = response.text

soup = BeautifulSoup(moisturizer, "html.parser")

price_w = soup.find("span", class_="a-price-whole").getText()
price_f = soup.find("span", class_="a-price-fraction").getText()

price = float(price_w + price_f)
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 15

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
