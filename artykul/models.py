from django.db import models

class Artykul(models.Model):
    tytul = models.CharField(max_length=1024)
    opis = models.TextField()
    file = models.FileField(upload_to='documents/')
    data_publikacji = models.DateTimeField()
    
    def __str__(self):
        return self.tytul