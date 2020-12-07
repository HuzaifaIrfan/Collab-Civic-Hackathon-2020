from django.urls import path, include


app_name = 'Collab_App'

from . import views



urlpatterns = [
 path('', views.home_view, name='home_view'),
 path('about', views.about_view, name='about_view'),
 path('team', views.team_view, name='team_view'),



]
   

