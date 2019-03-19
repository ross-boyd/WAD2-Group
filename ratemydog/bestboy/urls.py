from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('vote/', views.vote, name='vote'),
    path('upload/', views.upload, name='upload'),
    path('profile/<username>/', views.profile, name='profile')
]
