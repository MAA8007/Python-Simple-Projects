import bs4, requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

titles= soup.find_all("h3", class_="title")
movies=[]
for tag in titles:
    print(tag.getText())


