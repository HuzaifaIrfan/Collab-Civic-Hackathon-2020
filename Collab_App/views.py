from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from other_settings import num_of_el_in_page


from Projects.models import Project

def home_view(request):

    context={}

    # users=User.objects.all()
    # for user in users:
    #     print(user.id)
    #     socialaccounts=user.socialaccount_set.all()
    #     for socialaccount in socialaccounts:
    #         print(socialaccount.extra_data['name'])



    all_projects=Project.objects.all().order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_projects,num_of_el_in_page)

    projects = new_paginator.page(page)

    context['projects']=projects

    return render(request,'Home.html',context)


def about_view(request):

    context={}


    # context['page_title']='About'


    return render(request,'About.html',context)




def team_view(request):
    context={}

    # context['page_title']='Our Team'

    return render(request,'Team.html',context)

