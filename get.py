from selenium import webdriver
from selenium.webdriver.common.by import By  # Yangi qator, By obyektini import qilish

# Brauzerni ishga tushirish
driver = webdriver.Chrome()

# Sahifani ochish
driver.get("https://kun.uz/uz/news")

# Yangilik sarlavhalarini olish
headlines = driver.find_elements(By.TAG_NAME, 'h2')  # Yangi usul

for headline in headlines:
    print(headline.text)

# Brauzerni yopish
driver.quit()
