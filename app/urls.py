from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    # /app/
    url( r'^$' , views.IndexView.as_view( ) , name='index' ) ,
    # /app/<project>/
    url( r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view( ) , name='detail' ) ,
    # /app/project/1/delete
    url( r'project/(?P<pk>[0-9]+)/delete/$' , views.ProjectDelete.as_view( ) , name='project-delete' ) ,
    # /app/project/2/
    # url( r'project/(?P<pk>[0-9]+)/$' , views.Project.as_view( ) , name='project-update' ) ,
    url( r'^profile/' , views.profile , name='profile' ) ,
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
