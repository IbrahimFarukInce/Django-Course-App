from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('courses/', views.course_list, name='courses',),

    
]