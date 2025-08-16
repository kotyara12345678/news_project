from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    anons = models.CharField('Анонс', max_length=50)
    full_text = models.TextField('Статья')
    image = models.ImageField('Фото', upload_to='articles_images/', blank=True, null=True)  #фото
    data = models.DateTimeField('Дата публикации', default=timezone.now)

    def __str__(self):
        return self.title