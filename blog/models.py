from django.db import models


class Free(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('date published')
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    download_url = models.CharField(max_length=250)
    YouTube_link = models.CharField(blank=False, max_length=250)

    def __str__(self):
        return self.title


class Paid(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('date published')
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    price = models.CharField(max_length=250)
    YouTube_link = models.CharField(blank=False, max_length=250)

    def __str__(self):
        return self.title
