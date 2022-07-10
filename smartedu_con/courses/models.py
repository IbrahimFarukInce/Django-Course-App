from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100 , unique=True, verbose_name='Kurs Adı', help_text='Kurs Adını Yazınız')
    description = models.TextField(blank=True , null=True)
    image = models.ImageField(upload_to = "courses/%Y/%m/%d/", default='courses/default-course-image.jpg')
    date = models.DateTimeField(auto_now= True)
    availible = models.BooleanField(default=True)

    def __str__(self):
        return self.name