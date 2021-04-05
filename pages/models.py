from django.db import models
from django.urls import reverse


class Content(models.Model):
    title = models.CharField(max_length=200)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:content-detail', kwargs={'pk': self.pk})


class Video(Content):
    url_video = models.URLField()
    url_subtitles = models.URLField()


class Audio(Content):
    bitrate = models.IntegerField()


class Text(Content):
    content_text = models.TextField()


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.ManyToManyField(Content, related_name="pages",  blank=True)
    counter = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:page', kwargs={'pk': self.pk})

