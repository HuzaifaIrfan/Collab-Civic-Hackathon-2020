


from django.urls import path, re_path

from . import views
from django.urls import include




urlpatterns = [

    path('', views.all_projects),

    path('bystudent/<int:student_id>', views.student_projects_view),

    path('byuni/<int:uni_id>', views.uni_projects_view),

    path('<int:project_id>', views.project_view),
    
]