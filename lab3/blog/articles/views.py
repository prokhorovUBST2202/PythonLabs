from django.shortcuts import render
from .models import Article


# Представление, которое показывает архив всех статей
def archive(request):
    # Получаем все объекты Article из базы данных
    all_posts = Article.objects.all()

    # Готовим словарь с данными, которые передадим в шаблон
    context = {
        "posts": all_posts
    }

    # Возвращаем HTML-страницу archive.html с переданными данными
    return render(request, 'archive.html', context)
