


from django.urls import path, re_path

from . import views
from django.urls import include




urlpatterns = [

    path('', views.all_unis),

    path('<int:uni_id>', views.uni_view),
    
]