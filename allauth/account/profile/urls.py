
from django.urls import path, include

from . import views

app_name = 'profile'

urlpatterns = [


    path(
        "",
        views.profile,
        name="account_profile",
    ),


            path(
        "edit",
        views.profile_edit,
        name="profile_edit",
    ),


            path(
        "add_project",
        views.add_project,
        name="add_project",
    ),


    path(
        "my_projects",
        views.my_projects,
        name="my_projects",
    ),

    path(

        "edit_project/<int:project_id>",
        views.edit_project,
        name="edit_project",
    ),

    path(

        "delete_project/<int:project_id>",
        views.delete_project,
        name="delete_project",
    ),


    # path(
    #     "Get_Extra_Data",
    #     views.Get_Extra_Data,
    #     name="Get_Extra_Data",
    # ),

    # path(
    #     "Check_Auth_Info",
    #     views.Check_Auth_Info,
    #     name="Check_Auth_Info",
    # ),

    # path(
    #     "Refetch",
    #     views.Refetch,
    #     name="Refetch",
    # ),


    #     path(
    #     "Verify_Org",
    #     views.Verify_Org,
    #     name="Verify_Org",
    # ),





    #             path(
    #     "available_repo",
    #     views.available_repo,
    #     name="available_repo",
    # ),


    #             path(
    #     "projects",
    #     views.projects,
    #     name="projects",
    # ),



]