from django.shortcuts import render

# Create your views here.


from Universities.models import Universities,Departments,Batches

from .models import Project


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from other_settings import num_of_el_in_page

def all_projects(request):

    context={}


    all_projects=Project.objects.all().order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_projects,num_of_el_in_page)

    projects = new_paginator.page(page)

    context['projects']=projects

    context['page_title']='All Projects'

    return(render(request,'projects/list_view.html',context))





def student_projects_view(request,student_id):

    context={}


    all_projects=Project.objects.filter(social_user=student_id).order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_projects,num_of_el_in_page)

    projects = new_paginator.page(page)

    context['projects']=projects

    context['page_title']='Student Projects View'

    return(render(request,'projects/list_view.html',context))




def uni_projects_view(request,uni_id):

    context={}


    all_projects=Project.objects.filter(university=uni_id).order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_projects,num_of_el_in_page)

    projects = new_paginator.page(page)

    context['page_title']='Uni Projects View'

    context['projects']=projects


    return(render(request,'projects/list_view.html',context))





def project_view(request,project_id):

    context={}

    project=Project.objects.get(id=project_id)
    
    context['project']=project

    return(render(request,'projects/view.html',context))



