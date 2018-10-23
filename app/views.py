from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse , Http404
import datetime
import datetime as dt
from django.core.urlresolvers import reverse
from .models import Project , Profile,Review,Comment
from .forms import EditProfileForm , UploadForm,ReviewForm,CommentForm,UserForm
from django.contrib.auth.models import User


# Create your views here.

@login_required( login_url='/accounts/login/' )
def home(request):
    '''
    Method that fetches all images from all users.
    '''
    date=dt.date.today( )
    profile=Profile.objects.all
    project=Project.objects.all()
    comments=Comment.objects.all()
    form=CommentForm( )
    return render( request , 'index.html' , {
        "profile": profile ,
        "project": project ,
        "date":date,
        "comment":form,
        "comments":comments} )

@login_required( login_url='/accounts/login/' )
def profile(request):
    '''
    	Method that fetches a users profile page
    	'''
    current_user=request.user
    profile=Profile.get_profile( )
    project=Project.objects.all()
    comments=Comment.objects.all()
    return render( request , 'profile/profile.html' , {
        "comments": comments ,
        "project": project ,
        "user": current_user ,
        "profile": profile , } )


@login_required( login_url='/accounts/login/' )
def settings(request):
    '''
    	Method that fetches the details of a user uniquily
    	'''
    settings=Profile.get_profile( )
    return render( request , 'profile/setting.html' , {"settings": settings} )


@login_required( login_url='/accounts/login/' )
def edit(request):
    current_user=request.user
    if request.method == 'POST':
        form=EditProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'home' )
    else:
        form=EditProfileForm()
    return render( request , 'profile/edit.html' , {
        "form": form} )


@login_required( login_url="/accounts/login/" )
def upload(request):
    '''
    	Method that return a form for uploading profile
    	'''
    current_user=request.user
    profiles=Profile.get_profile( )
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form=UploadForm( request.POST , request.FILES )
                if form.is_valid( ):
                    upload=form.save( commit=False )
                    upload.user=current_user
                    upload.profile=profile
                    upload.save( )
                    return redirect( 'home' )
            else:
                form=UploadForm( )
            return render( request , 'upload/new-upload.html' , {
                "user": current_user ,
                "form": form} )



@login_required( login_url="/accounts/login/" )
@login_required( login_url='/accounts/login/' )
def search(request):
    '''
	Method that searches for users based on their profiles
	'''
    if request.GET['search']:
        search_term=request.GET.get( "search" )
        profiles=Profile.objects.filter( user__username__icontains=search_term )
        message=f"{search_term}"

        return render( request , 'search.html' , {"message": message , "profiles": profiles} )
    else:
        message="You haven't searched for any item"
        return render( request ,'search.html' , {"message": message} )


@login_required( login_url='/accounts/login/' )
def new_comment(request , pk):
    '''
    	Method that fetches a users new comment from the comment form
    	'''
    project=get_object_or_404( Project , pk=pk )
    current_user=request.user
    if request.method == 'POST':
        form=CommentForm( request.POST )
        if form.is_valid( ):
            comment=form.save( commit=False )
            comment.project=project
            comment.user=current_user
            comment.save( )
            return redirect( 'home' )
    else:
        form=CommentForm( )
    return render( request , 'comment.html' , {"user": current_user ,
                                               "comment_form": form} )


@login_required( login_url="/accounts/login/" )
def view_profile(request , pk):
    '''
    	Method that dispalys users profile only after creating profile
    	'''
    current_user=request.user
    project=Project.objects.all()
    profile=Profile.objects.all( )
    comment=Comment.objects.all( )
    user=get_object_or_404( User , pk=pk )
    return render( request , 'profile/view-profile.html' , {"user": current_user ,
                                            "project": project ,
                                            "my_user": user ,
                                            "comments": comment ,
                                            "profile": profile} )

class ProjectUpdate(UpdateView):
    model=Project

    template_name = 'album_form.html'
    fields = ['name', 'image','description','link']

class ProjectDelete(DeleteView):
    model=Project
    success_url = reverse_lazy('home')

def search(request):
    '''
	Method that searches for users based on their project
	'''
    if request.GET['search']:
        search_term=request.GET.get( "search" )
        projects=Project.objects.filter( name__icontains=search_term )
        message=f"{search_term}"

        return render( request , 'search.html' , {"message": message , "projects": projects} )
    else:
        message="You haven't searched for any item"
        return render( request ,'search.html' , {"message": message})
