from django.utils import timezone
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Категорія', max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField(unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Категорія для публікацій'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list', kwargs={'slug': self.slug})
        except:
            url = "/"
        return url


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField(unique_for_date='pub_date')
    description = models.TextField(blank=True, verbose_name='Опис')
    text = models.TextField('Текст', blank=True)
    pub_date = models.DateTimeField('Дата публікації', default=timezone.now)
    main_page = models.BooleanField('Головна', default=True, help_text='Показувати на головній сторінці')
    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            return reverse('news-detail', kwargs={'year': self.pub_date.strftime("%Y"),
                                                 'month': self.pub_date.strftime("%m"),
                                                 'day': self.pub_date.strftime("%d"),
                                                 'slug': self.slug})
        except:
            return "/"

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    title = models.CharField('Підпис', max_length=250, help_text='Максимум 250 символів', blank=True)

    class Meta:
        verbose_name = 'Фото до статті'
        verbose_name_plural = 'Фото до статей'

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.image.name.split('/')[-1]