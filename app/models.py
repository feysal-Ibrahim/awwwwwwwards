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
    user=models.ForeignKey( User , on_delete=models.CASCADE,related_name='profile',null=True )

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save( )

    def delete_profile(self):
        self.delete( )

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls , search_term):
        profile=cls.objects.filter( user__username__icontains=search_term )
        return profile

# user post model
class Project( models.Model ):
    objects=None
    name=models.CharField( max_length=30 )
    image=models.ImageField( upload_to='images/', blank=True )
    description=HTMLField( blank=True )
    link=models.URLField( blank=True )
    profile=models.ForeignKey( Profile , on_delete=models.CASCADE , null=True )
    user=models.ForeignKey( User , null=True )
    date=models.DateTimeField( auto_now_add=True )
    is_favorite=models.BooleanField( default=False )


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    @property
    def image_url(self):
        if self.image and hasattr( self.image , 'url' ):
            return self.image.url
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

class Review( models.Model ):
    RATING_CHOICES=(
        (1 , '1') ,
        (2 , '2') ,
        (3 , '3') ,
        (4 , '4') ,
        (5 , '5') ,
        (6 , '6') ,
        (7 , '7') ,
        (8 , '8') ,
        (9, '9') ,
        (10, '10') ,
    )
    project=models.ForeignKey( Project )
    pub_date=models.DateTimeField( 'date published' )
    user_name=models.CharField( max_length=100 )
    comment=models.CharField( max_length=200 )
    rating=models.IntegerField( choices=RATING_CHOICES )

class Comment(models.Model):
    objects=None
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,null=True)
    project = models.ForeignKey(Project,related_name='comment',null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
            self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ["-id"]