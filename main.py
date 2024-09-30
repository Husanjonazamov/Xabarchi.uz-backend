import requests
from bs4 import BeautifulSoup

# Ma'lumot tortib olinadigan sayt URLsi
url = "https://kun.uz/uz/news"

# Sahifani yuklash
response = requests.get(url)

# Sahifaning HTML kodini olish
soup = BeautifulSoup(response.text, 'html.parser')

# Yangilik sarlavhalarini olish (masalan, h2 teglari ichida bo'lsa)
headlines = soup.find_all('h2')

# Yangilik sarlavhalarini ko'rsatish
for headline in headlines:
    print(headline.text.strip())
