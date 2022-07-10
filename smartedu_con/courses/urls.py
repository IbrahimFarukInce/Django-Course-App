from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('courses/', views.course_list, name='courses',),
    path('courses/<slug:category_slug>/<int:course_id>', views.course_detail , name='course_detail',),

    
]