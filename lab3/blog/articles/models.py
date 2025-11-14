from django.db import models
from django.contrib.auth.models import User


# Модель одной статьи в блоге
class Article(models.Model):
    # Поле для заголовка статьи (строка длиной до 200 символов)
    title = models.CharField(max_length=200)

    # Поле для автора статьи.
    # Связь с встроенной моделью пользователя Django.
    # on_delete=models.CASCADE означает, что если пользователя удалить,
    # то его статьи тоже будут удалены.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Поле для основного текста статьи
    text = models.TextField()

    # Поле для даты создания статьи.
    # auto_now_add=True ставит дату автоматически при создании записи.
    created_date = models.DateField(auto_now_add=True)

    # Метод строкового представления объекта.
    # В старых примерах используется __unicode__.
    def __unicode__(self):
        # Возвращаем строку вида "имя_пользователя: заголовок"
        return "%s: %s" % (self.author.username, self.title)

    # Метод, который возвращает короткий текст статьи
    def get_excerpt(self):
        # Если текст длиннее 140 символов, обрежем его и добавим "..."
        if len(self.text) > 140:
            short_text = self.text[:140] + "..."
            return short_text

        # Если текст и так короткий, просто возвращаем его без изменений
        return self.text
