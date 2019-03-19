from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('vote/', views.vote, name='vote'),
    path('upload/', views.upload, name='upload'),
    #path('profile/', views.profile, name='profile')
]
