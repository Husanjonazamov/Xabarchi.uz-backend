import requests
from bs4 import BeautifulSoup

# Kun.uz RSS manzili
rss_url = "https://kun.uz/uz/news/rss"

# Sahifani yuklab olish
response = requests.get(rss_url)

# Agar muvaffaqiyatli yuklansa
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'xml')  # RSS XML formatda keladi, shuning uchun 'xml' parser ishlatiladi

    # RSS dan yangiliklarni qidiramiz
    items = soup.find_all('item')  # 'item' teglarida yangiliklar mavjud

    # Har bir yangilikni chiqaramiz
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        pub_date = item.find('pubDate').text
        description = item.find('description').text

        print(f"Sarlavha: {title}")
        print(f"Havola: {link}")
        print(f"Chop etilgan sana: {pub_date}")
        print(f"Tavsif: {description}")
        print("-" * 50)

else:
    print(f"Xato: {response.status_code}")
