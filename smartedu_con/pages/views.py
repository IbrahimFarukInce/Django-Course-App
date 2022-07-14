import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from courses.models import Course

# def index(request): 
#     return render(request , 'index.html')
    
# def about(request):
#     return render(request , 'about.html')

class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(availible = True).order_by('-date')[:2]
        context['total'] = Course.objects.filter(availible = True).count()
        return context

class Aboutview(TemplateView):
    template_name = 'about.html'

# Create your views here.
