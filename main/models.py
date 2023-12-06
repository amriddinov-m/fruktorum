from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    class Meta:
        abstract = True


class Bookmark(BaseModel):
    class LinkType(models.TextChoices):
        website = 'website', 'Веб-сайт'
        book = 'book', 'Книга'
        article = 'article', 'Статья'
        music = 'music', 'Музыка'
        video = 'video', 'Видео'

    title = models.CharField(verbose_name='Заголовок страницы', max_length=255, blank=True)
    description = models.TextField(verbose_name='Краткое описание', blank=True)
    url = models.URLField(verbose_name='Ссылка на страницу')
    link_type = models.CharField(verbose_name='Тип ссылки',
                                 max_length=255,
                                 choices=LinkType.choices,
                                 default=LinkType.website)
    preview_image = models.URLField(verbose_name='Картинка превью', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Закладка'
        verbose_name_plural = 'Закладки'


class Collection(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    bookmarks = models.ManyToManyField(Bookmark, related_name='collections', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
