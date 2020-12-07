
from django.urls import path, re_path

from . import views
from django.urls import include

app_name = 'Search'


urlpatterns = [

    path('', views.search_projects, name='search_projects'),

     path('advance', views.advance_search),


    # path('byuni/<int:uni_id>', views.uni_students_view),

    # path('<int:student_id>', views.student_view),
    
]