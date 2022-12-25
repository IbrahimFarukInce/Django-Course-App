from re import T
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = "teachers/%Y/%m/%d/")
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self) :
        return self.name


0