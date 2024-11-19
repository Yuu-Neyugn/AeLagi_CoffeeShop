from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    # url Index
    path('', views.IndexView.as_view(), name='index'),
    # url About us
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
]