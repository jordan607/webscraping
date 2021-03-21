from bs4 import BeautifulSoup
import requests
import lxml


text=[]
link=[]
score=[]
response = requests.get("https://news.ycombinator.com/newest")
data = response.text

soup = BeautifulSoup(data, "lxml")
news_title = soup.findAll(name="a", class_="storylink")
for news in news_title:
    article_text = news.getText()
    text.append(article_text)
    article_link = news.get("href")
    link.append(article_link)

news_score =  soup.findAll(name="span", class_="score")

score = [int(points.getText().split()[0]) for points in news_score ]

# print(text)
# print(link)
# print(score)

largest_number = max(score)
largest_index = score.index(largest_number)

print(text[largest_index])
print(link[largest_index])







# import lxml
#
# with open("website.html", encoding="utf8") as file:
#     data = file.read()
#
# # html.parser
# soup = BeautifulSoup(data, "lxml")
# print(soup.title.string)
# anchor_tags = soup.findAll(name="a")
# for tags in anchor_tags:
#     print(tags.getText())
#     print(tags.get("href"))
#
# # finding by id/class_
#
# h1_tag = soup.find(name="h1",id="name")
# h3_tag = soup.find(name="h3",class_="heading")
# print(h1_tag.string)
# print(h3_tag.string)
#
# company_url = soup.select_one("p a")
# print(company_url)
#
# soup.select(".heading")
# soup.select_one("#name")
