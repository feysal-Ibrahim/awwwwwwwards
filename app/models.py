from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
import datetime as dt


# Create your models here.

# user profile model
class Profile( models.Model ):
    objects=None
    profilePic=models.ImageField( upload_to='profile/' , null=True , blank=True )
    contact=HTMLField( )
    bio=models.CharField( max_length=60 , blank=True )
    user=models.ForeignKey( User , on_delete=models.CASCADE )

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save( )

    def delete_profile(self):
        self.delete( )

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all( )
        return profile

    @classmethod
    def find_profile(cls , search_term):
        profile=cls.objects.filter( user__username__icontains=search_term )
        return profile

# user post model
class Project( models.Model ):
    objects=None
    name=models.CharField( max_length=30 )
    image=models.ImageField( upload_to='images/' , blank=True )
    description=HTMLField( blank=True )
    link=models.URLField( blank=True )
    profile=models.ForeignKey( Profile , on_delete=models.CASCADE , null=True )
    user=models.ForeignKey( User , on_delete=models.CASCADE )
    date=models.DateTimeField( auto_now_add=True )


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @classmethod
    def search_by_name(cls , search_term):
        projects=cls.objects.filter( name__icontains=search_term )
        return projects

    @classmethod
    def one_post(cls , id):
        projects=Project.objects.filter( id=id )
        return projects

    @classmethod
    def all_posts(cls):
        projects=cls.objects.all( )
        return projects

    @classmethod
    def get_user_posts(cls , profile_id):
        images=Project.objects.filter( profile_id=id )
        return images

    @classmethod
    def get_profile_image(cls , profile):
        posts=Project.objects.filter( user__pk=profile )
        return posts

    @classmethod
    def get_project_by_id(cls , id):
        projects=Project.objects.filter( id=Project.id )
        return projects

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all( )
        return profile

    @classmethod
    def get_project(cls):
        project=Project.objects.all()
        return project


