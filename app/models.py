from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt


# Create your models here.

class Profile( models.Model ):
    profilePic=models.ImageField( upload_to='profile/' , null=True , blank=True )
    contact = HTMLField()
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
class Post(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True)
    description = HTMLField(blank=True)
    link=models.URLField(blank=True)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_name(cls,search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def one_post(cls, id):
        post=Post.objects.filter(id=id)
        return post

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def get_user_posts(cls, profile_id):
        images=Post.objects.filter(profile_id=id)

    @classmethod
    def get_profile_image(cls, profile):
        posts = Post.objects.filter(user_profile__pk=profile)
        return posts

    @classmethod
    def get_post_by_id(cls,id):
        post = Post.objects.filter(id = Post.id)
        return post

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile