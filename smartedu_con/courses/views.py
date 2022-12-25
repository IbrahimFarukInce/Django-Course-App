from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . models import Category, Course, Tag
from django.db.models import Q

def course_list(request, category_slug=None, tag_slug=None):

    search_course = request.GET.get('search')
   
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if search_course :
        courses = Course.objects.filter(Q(name__icontains = search_course) | Q(description__icontains = search_course) )

    elif category_slug != None :
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(availible=True, category = category_page).order_by('-date')

    elif tag_slug != None :
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(availible=True, tags = tag_page).order_by('-date')

    else :
        courses = Course.objects.all().order_by('-date')
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = { 
        'courses': courses,
        'categories':categories,
        'tags':tags
    }

    return render(request, 'courses.html', context)



def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id =course_id)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = { 
        'course': course,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'course-single.html', context)





# def course_list(request):
#     search_course = request.GET.get('search')
#     if search_course :
#         courses = Course.objects.filter(Q(name__icontains = search_course) | Q(description__icontains = search_course) )
#     else :
#         courses = Course.objects.all().order_by('-date')
        
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = { 
#         'courses': courses,
#         'categories':categories,
#         'tags':tags
#     }


#     return render(request, 'courses.html', context)

# def courses_by_category(request, category_slug):
#     courses = Course.objects.all().filter(category__slug = category_slug)
#     tags = Tag.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'courses': courses,
#         'tags': tags,
#         'categories': categories,


#     }
#     return render( request , 'courses.html', context)


# def courses_by_tag(request, tag_slug):
#     courses = Course.objects.all().filter(tags__slug=tag_slug)

#     categories = Category.objects.all()
#     tags = Tag.objects.exclude(slug=tag_slug)

#     context = { 
#         'courses': courses,
#         'categories':categories,
#         'tags':tags
#     }
#     return render(request, 'courses.html', context)