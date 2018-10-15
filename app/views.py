from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project , Profile
from .forms import EditProfileForm , UploadForm
from django.contrib.auth.models import User


# Create your views here.
@login_required( login_url='/accounts/login/' )
def home(request):
    '''
    Method that fetches all images from all users.
    '''
    current_user=request.user
    profile=Profile.objects.all
    project=Project.objects.all()
    return render( request , 'index.html' , {
        "profile": profile ,
        "current_user": current_user ,
        "project": project , } )


@login_required( login_url='/accounts/login/' )
def profile(request):
    '''
    	Method that fetches a users profile page
    	'''
    current_user=request.user
    profile=Profile.objects.all( )
    project=Project.objects.all()
    return render( request , 'profile/profile.html' , {
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
            return redirect( 'profile' )
    else:
        form=EditProfileForm( )
    return render( request , 'profile/edit.html' , {
        "form": form} )



@login_required( login_url="/accounts/login/" )
def create(request):
    '''
    	Method that return a form for uploading project
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



@login_required( login_url="/accounts/login/" )
def view_profile(request , pk):
    '''
    	Method that dispalys users profile only after creating profile
    	'''
    current_user=request.user
    project=Project.get_project()
    profile=Profile.get_profile( )
    user=get_object_or_404( User , pk=pk )
    return render( request , 'profile/view-profile.html' , {"user": current_user ,
                                            "project": project ,
                                            "my_user": user ,
                                            "profile": profile} )


@login_required( login_url="/accounts/login/" )
def like(request , operation , pk):
    '''
    Method function that likes a post.
    '''
    project=get_object_or_404( request,Project , pk=pk )
    if operation == 'like':
        project.likes+=1
        project.save( )
    elif operation == 'unlike':
        project.likes-=1
        project.save( )
    return redirect( 'home' )
