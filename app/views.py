from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login
from django.views.generic import View
from django.shortcuts import render , redirect , get_object_or_404
from .models import Project,Profile

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'award/index.html'
    context_object_name = 'all_project'

    def get_queryset(self):
        return Project.objects.all()

class DetailView(generic.DetailView):
    model = Project
    template_name = 'award/detail.html'

class ProjectDelete(DeleteView):
    model=Project
    success_url = reverse_lazy('index')


def profile(request):
    '''
    	Method that fetches a users profile page
    	'''
    current_user=request.user
    profile=Profile.get_profile( )
    project=Project.get_peoject( )
    return render( request , 'award/profile.html' , {
        "project": project ,
        "user": current_user ,
        "profile": profile , } )
