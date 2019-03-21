from django.urls import path
from django.conf.urls import url
from . import views
from ratemydog import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('vote/', views.vote, name='vote'),
    path('upload/', views.upload, name='upload'),
    path('profile/<username>/', views.profile, name='profile'),
    path('dog/<dogid>/', views.dogprofile, name='dogprofile'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
