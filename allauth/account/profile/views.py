# Create your views here.
from django.http import HttpResponse,JsonResponse




from django.shortcuts import render

from django.shortcuts import redirect



from allauth.socialaccount.models import SocialAccount, SocialToken



import json

import requests




from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import FormView




from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from allauth.socialaccount.forms import edit_profile_form

from Projects.forms import add_project_form, edit_project_form

from Projects.models import Project


def profile(request):

    return render(request,'profile/profile.html')


    

def my_projects(request):

    context={}


    if request.user.is_authenticated:
        user = request.user


        all_my_projects=Project.objects.filter(user=user).order_by("-id")


        try:
            page=int(request.GET.get('page'))
        except:
            page=1



        new_paginator=Paginator(all_my_projects,3)

        projects = new_paginator.page(page)

        context['projects']=projects


        return render(request,'profile/my_projects.html',context)


        



    



def profile_edit(request):

    context={}
    


    if request.user.is_authenticated:
        user = request.user
        social_account_user=user.socialaccount_set.all()[0]


        



        if request.method =="POST":

            try:
                form_data=request.POST
                # form_files=request.FILES


                # form=edit_profile_form(form_data,form_files,instance=social_account_user)

                form=edit_profile_form(form_data,instance=social_account_user)

                form.save()

                context['message']={'success':True,'message':'Saved'}

            except:

                context['message']={'success':False,'message':'Error Occurred'}

        else:

            form=edit_profile_form(instance=social_account_user)

        context['form']=form


    return render(request,'profile/edit.html',context)






def add_project(request):


    context={}


    if request.user.is_authenticated:
        user = request.user
        social_account_user=user.socialaccount_set.all()[0]


        



        if request.method =="POST":

            project = Project.objects.create(user=user)

            try:
                form_data=request.POST
                form_files=request.FILES




                # form=edit_profile_form(form_data,form_files,instance=social_account_user)

                form=add_project_form(form_data,form_files,instance=project)

                form.save()

                context['message']={'success':True,'message':'Project Added'}

            except:

                

                context['message']={'success':False,'message':'Error Occurred'}

        else:

            form=add_project_form()

        context['form']=form




    return render(request,'profile/add_project.html',context)




def delete_project(request,project_id):

    


    context={}


    if request.user.is_authenticated:

        try:
        
            user = request.user
            social_account_user=user.socialaccount_set.all()[0]
            project=Project.objects.get(id=project_id)

            if project.user == user:

                project.delete()
                context['message']="Project Deleted!!"

            else:

                context['message']="You don't own this Project"

        except:
            context['message']="Project Not Found"
    
    return render(request,'danger.html',context)






def edit_project(request,project_id):

    


    context={}


    if request.user.is_authenticated:
        
        user = request.user
        social_account_user=user.socialaccount_set.all()[0]
        project=Project.objects.get(id=project_id)
        


        



        if request.method =="POST":

            # project = Project.objects.create(user=user)

            try:
                form_data=request.POST
                form_files=request.FILES




                # form=edit_profile_form(form_data,form_files,instance=social_account_user)

                form=edit_project_form(form_data,form_files,instance=project)

                form.save()

                context['message']={'success':True,'message':'Project Editted'}

            except:

                

                context['message']={'success':False,'message':'Error Occurred'}

        else:

            form=edit_project_form(instance=project)

        context['form']=form




    return render(request,'profile/edit_project.html',context)




