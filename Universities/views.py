from django.shortcuts import render

# Create your views here.


from .models import Universities,Departments,Batches


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def all_unis(request):

    context={}


    all_unis=Universities.objects.all().order_by("-id")


    try:
        page=int(request.GET.get('page'))
    except:
        page=1



    new_paginator=Paginator(all_unis,3)

    unis = new_paginator.page(page)

    context['unis']=unis


    return(render(request,'unis/list_view.html',context))




def uni_view(request,uni_id):

    context={}

    uni=Universities.objects.get(id=uni_id)
    
    context['uni']=uni

    return(render(request,'unis/view.html',context))



