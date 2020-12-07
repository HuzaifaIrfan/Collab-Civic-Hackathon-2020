from django.shortcuts import render

# Create your views here.


from Universities.models import Universities,Departments,Batches

from allauth.socialaccount.models import SocialAccount


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def all_students(request):

    context={}


    all_students=SocialAccount.objects.all().order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_students,3)

    students = new_paginator.page(page)

    context['students']=students


    return(render(request,'students/list_view.html',context))






def uni_students_view(request, uni_id):

    context={}


    all_students=SocialAccount.objects.filter(university=uni_id).order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_students,3)

    students = new_paginator.page(page)

    context['students']=students


    return(render(request,'students/list_view.html',context))






def student_view(request,student_id):

    context={}

    student=SocialAccount.objects.get(id=student_id)
    
    context['student']=student

    return(render(request,'students/view.html',context))



