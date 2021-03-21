import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Firefox("./chromedriver")

URL = "https://www.empireonline.com/movies/features/best-movies-2"
sada = browser.get(URL)
time.sleep(3)
source = browser.page_source

# response = requests.get(URL)
# movie_data= response.text

soup = BeautifulSoup(source,"html.parser")
# movie_name = soup.find(name="h3")
print(soup.prettify())

#
# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
#
# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
#
# all_movies = soup.find_all(name="h3", class_="title")
#
# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]
#
# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")