from django.contrib import admin
from . models import Category, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ('name','availible','date')
    list_filter= ('availible',)
    search_fields= ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name',)
    prepopulated_fields= {'slug':('name',)}