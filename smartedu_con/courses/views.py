from unicodedata import category
from django.shortcuts import render
from . models import Category, Course
    
def course_list(request):
    courses = Course.objects.all().order_by('-date')
    context = { 
        'courses': courses
    }
    return render(request, 'courses.html', context)

def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id =course_id)
    categories = Category.objects.all()
    context = { 
        'course': course,
        'categories':categories
    }
    return render(request, 'course-single.html', context)