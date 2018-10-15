from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    # /app/
    url( r'^$' , views.IndexView.as_view( ) , name='index' ) ,
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
