import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from courses.models import Course
from . forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin


class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(availible = True).order_by('-date')[:2]
        context['total'] = Course.objects.filter(availible = True).count()
        return context

class Aboutview(TemplateView):
    template_name = 'about.html'


class ContactView(SuccessMessageMixin, FormView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    template_name = 'contact.html'
    form_class = ContactForm
    
    success_url = '/contact'
    success_message = "We received your request"

    def form_valid(self, form) :
        form.save()
        return super().form_valid(form)