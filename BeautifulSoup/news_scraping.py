from re import S
import requests, bs4
from bs4 import BeautifulSoup

article_titles = []
article_links = []

response = requests.get("https://news.ycombinator.com/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

x= soup.find_all(name="a",class_="titlelink")

for tag in x:
    text= tag.getText()
    article_titles.append(text)


for tag in x:
    link= tag.get("href")
    article_links.append(link)

for x in article_titles:
    print(x)