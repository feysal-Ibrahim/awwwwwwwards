from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # /app/project/homepage
    url( '^$' , views.home , name='home' ),

    # /app/project/id/profile
    url( r'^profile/' , views.profile , name='profile' ),

    # /app/project/id/edit
    url( r'^upload_project/' , views.upload , name='upload' ) ,

    # /app/project/id/edit
    url( r'^edit/' , views.edit , name='edit' ) ,

    # /app/project/id/user details
    url( r'^settings/' , views.settings , name='settings' ) ,
    # /app/project/search

    url( r'^search/' , views.search , name='search' ) ,

    # /app/project/id/view-profile
    url( r'^review/(?P<pk>\d+)' , views.new_comment , name='review' ) ,

    # /app/project/id/profile

    url( r'^view_profile/(?P<pk>\d+)' , views.view_profile , name='profile' ) ,

    # /app/project/id/update
    url( r'project/(?P<pk>[0-9]+)/$' , views.ProjectUpdate.as_view( ) , name='project-update' ) ,

    # /app/project/id/delete
    url( r'project/(?P<pk>[0-9]+)/delete/$' , views.ProjectDelete.as_view( ) , name='project-delete' ) ,
]

if settings.DEBUG:
    urlpatterns+=static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
