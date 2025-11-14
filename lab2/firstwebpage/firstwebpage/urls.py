"""
URL configuration for firstwebpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin   # импорт интерфейса админки
from django.urls import path # функция path добавляет адрес и связывает его с функцией-представлением
from flatpages.views import home, hello_page  # импорт наших функций из приложения flatpages (views.py)

urlpatterns = [
    path('admin/', admin.site.urls),   # адрес /admin/ ведёт в админку
    path('', home, name='home'),          # http://127.0.0.1:8000/  — это корень сайта /, вызывает функцию home
    path('hello/', hello_page, name='hello'),  # http://127.0.0.1:8000/hello/ вызывает функцию hello_page
]

