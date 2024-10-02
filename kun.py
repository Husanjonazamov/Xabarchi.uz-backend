import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_desc(link):
    base_url = "https://kun.uz{}".format(link)
    html = requests.get(base_url).content
    soup = BeautifulSoup(html, "html.parser")
    head = soup.find("div", {"class": "news-inner__content-head"})
    return head.find("div", {"class": "news-inner__content-page"}).text
    

def get_kun_uz_news():
    url = "https://kun.uz/news/category/uzbekiston"  # Asosiy yangiliklar sahifasi
    response = requests.get(url)
    
    if response.status_code == 200:  # Sahifa muvaffaqiyatli yuklanganini tekshiramiz
        soup = BeautifulSoup(response.content, 'html.parser')
        # Yangilik elementlarini topamiz
        news_list = soup.find_all('a', {"class": 'news-page__item'})  # Yangilik bloklarini topamiz
        news_items = []
        progress = tqdm(total=len(news_list))
        for news in news_list:
            img = news.find("div", {"class": "news-page__item-img"}).find("img")['src']
            title = news.find("h3", {"class": "news-page__item-title"}).text
            date = news.find("div",{"class": "gray-date"}).find("p").text
            link = news['href']
            news_items.append({
                "img": img,
                "title": title,
                "date": date,
                "link": link,
                "desc": get_desc(link)
            })
            progress.update(1)

        return news_items
    else:
        return {"error": f"HTTP xato: {response.status_code}"}

# Funksiyani chaqirib, natijani chiqaramiz
news = get_kun_uz_news()
for item in news:
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print(f"Image: {item['img']}")
    print(f"Date: {item['date']}")
    print(f"Desc: {item['desc']}")
    # print(f"Description: {item['description']}")
    print("----------")
