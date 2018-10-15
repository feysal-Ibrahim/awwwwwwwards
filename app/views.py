from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login
from django.views.generic import View
from .models import Project

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'award/index.html'
    context_object_name = 'all_post'

    def get_queryset(self):
        return Project.objects.all()
