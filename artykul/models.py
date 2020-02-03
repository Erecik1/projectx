from django.db import models
from django.utils import timezone

class Artykul(models.Model):
    Title = models.CharField(max_length=1024)
    Description = models.TextField()
    File = models.FileField(upload_to='documents/%Y/%m/%d')
    Date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul