from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import  authenticate,login
from django.views.generic import View
from django.contrib.auth.models import User
from django.shortcuts import render , redirect , get_object_or_404
from .models import Project,Profile

# Create your views here.
def index(request):
    '''
    Method that fetches all images from all users.
    '''
    current_user=request.user
    profile=Profile.get_profile( )
    project=Project.get_project()
    return render( request , 'award/index.html' , {
        "profile": profile ,
        'project':project,
        "current_user": current_user ,} )
