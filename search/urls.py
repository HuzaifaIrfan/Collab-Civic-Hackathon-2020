
from django.urls import path, re_path

from . import views
from django.urls import include




urlpatterns = [

    path('', views.advance_search),


    # path('byuni/<int:uni_id>', views.uni_students_view),

    # path('<int:student_id>', views.student_view),
    
]