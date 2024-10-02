# tasks.py
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import News

def get_desc(link):
    base_url = "https://kun.uz{}".format(link)
    html = requests.get(base_url).content
    soup = BeautifulSoup(html, "html.parser")
    head = soup.find("div", {"class": "news-inner__content-head"})
    return head.find("div", {"class": "news-inner__content-page"}).text



@shared_task
def fetch_and_save_news():
    url = "https://kun.uz/news/category/uzbekiston"  # Asosiy yangiliklar sahifasi
    response = requests.get(url)
    
    if response.status_code == 200:  # Sahifa muvaffaqiyatli yuklanganini tekshiramiz
        soup = BeautifulSoup(response.content, 'html.parser')
        # Yangilik elementlarini topamiz
        news_list = soup.find_all('a', {"class": 'news-page__item'})  # Yangilik bloklarini topamiz
        
        for news in news_list:
            img = news.find("div", {"class": "news-page__item-img"}).find("img")['src']
            title = news.find("h3", {"class": "news-page__item-title"}).text
            date = news.find("div",{"class": "gray-date"}).find("p").text
            link = news['href']
            desc = get_desc(link)  # Tavsifni olish
            
            # Yangilikni saqlash
            News.objects.get_or_create(
                title=title,
                description=desc,
                image_url=img,
                link=link
            )
    else:
        print(f"HTTP xato: {response.status_code}")
