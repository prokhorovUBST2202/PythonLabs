from django.contrib import admin
from .models import Article


# Класс, который описывает, как модель Article показывается в админке
class ArticleAdmin(admin.ModelAdmin):
    # Поля, которые будут показаны в списке статей
    list_display = ('title', 'author', 'get_excerpt', 'created_date')


# Регистрация модели Article в административном интерфейсе
# вместе с настройками ArticleAdmin
admin.site.register(Article, ArticleAdmin)
