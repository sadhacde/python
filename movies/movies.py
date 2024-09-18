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
print(number)
print(article_texts[index])
print(article_links[index])













'''
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

soup.title => <title>Content</title>
soup.title.name => title
soup.title.string => Content
soup.a => first <a> tag line
soup => full html file (prettify indents it)

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())

soup.find_all(name="a") => list of all anchor tags
tag.getText() => all text of a particular tag
tag.get("href") => all links. or whatever attribute

soup.find(name="h1", id="name") => based on id

soup.find(name="h3", class_="heading" => based on class
section_heading.get("class") => class name

CSS Selectors
company_url = soup.select_one(selector="p a") => anchor within a paragraph tag

name = soup.select_one("#name") => all tags with id="name"
headings = soup.select(".heading") => list of tags with class="heading"

'''
