from django.http import HttpResponse      # класс простого текстового ответа (здесь оставлен на случай заданий)
from django.shortcuts import render       # функция render "рендерит" (собирает) HTML-шаблон и возвращает его как ответ
from django import template               # модуль шаблонов Django (импортирован для наглядности)

def home(request):
    # request — объект запроса от браузера (какой адрес открыл, какие заголовки и т.д.)
    # Возвращаем рендер шаблона index.html из папки templates нашего приложения.
    # Строка 'templates/index.html' — путь к файлу шаблона внутри приложения flatpages.
    # корневая страница без стилей
    return render(request, 'templates/index.html')

def hello_page(request):
    # Вторая страница из задания — та же разметка, но со стилями и картинкой.
    # Рендерим шаблон static_handler.html из той же папки templates.
    # страница со стилями и логотипом
    return render(request, 'templates/static_handler.html')