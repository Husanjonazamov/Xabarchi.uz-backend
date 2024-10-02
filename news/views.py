from django.http import JsonResponse
from rest_framework.decorators import api_view
from .task import fetch_and_save_news
from .models import News
from rest_framework import status




@api_view(['POST'])
def trigger_news_fetch(request):
    # Celery vazifasini ishga tushirish
    fetch_and_save_news.delay()
    return JsonResponse({"status": "Yangiliklar olish vazifasi yuborildi!"}, status=status.HTTP_202_ACCEPTED)




@api_view(['GET'])
def get_news(request):
    # Yangiliklar ro'yxatini olish
    news_items = News.objects.all().order_by('-published_on')
    news_list = []
    for news in news_items:
        news_list.append({
            "title": news.title,
            "image_url": news.image_url,
            "link": news.link,
            "published_on": news.published_on,
            "description": news.description  # Tavsifni qo'shamiz
        })
    return JsonResponse(news_list, safe=False, status=status.HTTP_200_OK)


from django.shortcuts import render

@api_view(['GET'])
def get_news(request):
    # Yangiliklar ro'yxatini olish
    news_items = News.objects.all().order_by('-published_on')
    return render(request, 'base.html', {'news_items': news_items})
