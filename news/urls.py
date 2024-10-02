from django.urls import path
from .views import trigger_news_fetch, get_news

urlpatterns = [
    path('api/trigger-news-fetch/', trigger_news_fetch, name='trigger-news-fetch'),
    path('', get_news, name='get-news'),  # Yangiliklar sahifasi
]
