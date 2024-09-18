'''
webscrapes 100 greatest movies and lists them in a txt file to act as a checklist!
'''

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empireon = response.text

soup = BeautifulSoup(empireon, "html.parser")

titles = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in titles]
movies.reverse()

with open('movies.txt', 'w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
