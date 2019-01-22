from django.urls import path
from . import views
urlpatterns = [
    path('', views.top, name='top'),
    path('tweet_list/', views.tweet_list, name='tweet_list'),
    path('profile/', views.profile, name='profile'),
    path('help/', views.help, name='help'),
    path('tweet_add/', views.tweet_add, name='tweet_add'),
    path('policy/', views.policy, name='policy'),
]