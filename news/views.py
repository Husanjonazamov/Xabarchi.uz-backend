from rest_framework import viewsets
from rest_framework.response import Response
from .models import News
from api.serializers import NewsSerializer
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class NewsViewSet(viewsets.ViewSet):
    def list(self, request):
        url = "https://kun.uz/uz/news/rss"  # Yangiliklar RSS manzili
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # HTTP xatoliklarini aniqlash
            
            # XML ma'lumotlarni tahlil qilish uchun BeautifulSoup ishlatamiz
            soup = BeautifulSoup(response.content, 'xml')
            
            # Yangiliklarni chiqarish
            news_items = []
            items = soup.find_all('item')  # RSS ichida 'item' teglarini topamiz
            
            for item in items:
                title = item.find("title").text
                link = item.find("link").text
                pub_date = item.find("pubDate").text
                description = item.find("description").text

                # Vaqt formatini to'g'irlash
                try:
                    published_on = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
                except ValueError:
                    published_on = None  # Xato vaqt formatida bo'lsa None

                # Yangilikni qo'shish yoki yangilash
                news_item, created = News.objects.update_or_create(
                    title=title,
                    defaults={
                        'link': link,
                        'published_on': published_on,
                        'description': description,
                    }
                )

                # Har doim yangiliklar ro'yxatiga qo'shish
                news_items.append(news_item)

            response_data = {
                'total_news_fetched': len(items),  # Topilgan yangiliklar soni
                'new_news_added': len(news_items),  # Yangi yangiliklar
                'news': NewsSerializer(news_items, many=True).data
            }

            return Response(response_data)

        except requests.exceptions.RequestException as e:
            return Response({"error": f"HTTP xato: {e}"}, status=500)
        except Exception as e:
            return Response({"error": f"Noma'lum xato: {e}"}, status=500)
