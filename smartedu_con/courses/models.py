from re import T
from unicodedata import category
from django.db import models


# One to Many Realations with Course
class Category(models.Model):

    name = models.CharField(max_length=100, null=True , unique=True, verbose_name='Kategori')
    slug = models.SlugField(max_length=50, unique=True, null=True )

    def __str__(self):
        return self.name


# Many to Many Realations with Course
class Tag(models.Model):

    name = models.CharField(max_length=100, null=True , unique=True, verbose_name='Tag')
    slug = models.SlugField(max_length=50, unique=True, null=True )

    def __str__(self):
        return self.name


# One to Many Realations with Category
class Course(models.Model):

    name = models.CharField(max_length=100 , unique=True, verbose_name='Kurs Adı')
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING) #ForeignKey Column
    tags = models.ManyToManyField(Tag, blank=True, null=True, help_text='Birden fazla seçim yapmak için te "CTRL" veya "COMMAND" tuşuna basılı tutun.')
    description = models.TextField(blank=True , null=True)
    image = models.ImageField(upload_to = "courses/%Y/%m/%d/", default='courses/default-course-image.jpg')
    date = models.DateTimeField(auto_now= True)
    availible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
