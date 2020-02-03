from django.db import models
from django.utils import timezone


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=64, unique=True)

    class Meta():
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazwa


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=64)
    text = models.TextField()
    document = models.FileField(upload_to='documents/')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.PROTECT, null=True,
                                  blank=True, )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Image(models.Model):
    source = models.ImageField()
    name = models.CharField(max_length=64)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

