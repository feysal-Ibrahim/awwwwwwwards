from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url( '^$' , views.home , name='home' ) ,
    url( r'^profile/' , views.profile , name='profile' ),
    url( r'^search/' , views.search , name='search' ) ,
    url( r'^create_project/' , views.create , name='create' ) ,
    url( r'^edit/' , views.edit , name='edit' ),
    url( r'^settings/' , views.settings , name='settings' ) ,
    url( r'^view_profile/(?P<pk>\d+)' , views.view_profile , name='profile' ) ,
    url( r'^like/(?P<operation>.+)/(?P<pk>\d+)' , views.like , name='like' ),
]

if settings.DEBUG:
    urlpatterns+=static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
