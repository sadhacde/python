'''
displays article title and its link with the highest upvotes from
Hacker News - https://news.ycombinator.com/news
'''

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")
spans = soup.find_all("span", class_="titleline")

articles = []
for span in spans:
    articles.append(span.find("a"))

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

number = max(article_upvotes)
index = article_upvotes.index(number)

print(article_texts[index])
print(article_links[index])
