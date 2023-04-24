import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(rel.content,"html.parser")
movies=soup.find("tbody",class_="lister-list",).find_all("tr")
list=[]
for movie in movies:
    dic={"movie":"","year":"","rating":"","position":"","link":""}
    name=movie.find('td',class_="titleColumn").a.text
    ratings=movie.find('td',class_="ratingColumn imdbRating").strong.text
    position=movie.find("td",class_='titleColumn').get_text(strip=True).split('.')[0]
    year=movie.find("td",class_="titleColumn").span.text.strip("()") 
    url=movie.find("td",class_="titleColumn").a["href"]
    link="https://www.midb.com/"+url   
    dic["movie"]=name
    dic["year"]=year
    dic["rating"]=ratings
    dic["position"]=position
    dic["link"]=link
    list.append(dic)    
answer={}
a=[]
b=[]
c=[]
d=[]
i=0
while i<len(list):
    if list[i]["year"]>="1960" and list[i]["year"]<="1969":
        a.append(list[i])
        answer["1960"]=a
    if list[i]["year"]>="1970" and list[i]["year"]<="1979":
        b.append(list[i])
        answer["1970"]=b
    if list[i]["year"]>="1980" and list[i]["year"]<="1989":
        c.append(list[i])
        answer["1980"]=c
    
    if list[i]["year"]>="2000" and list[i]["year"]<="2009":
        d.append(list[i])
        answer["2000"]=d      
    i=i+1
with open("task_3.json","w")as f:
    json.dump(answer,f,indent=8)