from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from Projects.models import Project

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from other_settings import num_of_el_in_page


def advance_search(request):
    

    return(render(request,'search/advance.html'))



def search_projects(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:


            lookups= Q(full_name__icontains=query) | Q(description__icontains=query ) | Q(info__icontains=query )| Q(team__icontains=query )

            project_results= Project.objects.filter(lookups).distinct().order_by('-id')



            try:
                page=int(request.GET.get('page'))
            except:
                page=1



            new_paginator=Paginator(project_results,num_of_el_in_page)

            projects = new_paginator.page(page)




            context={'projects': projects,
                     'submitbutton': submitbutton}


            context['page_title']=f"Showing Search Results for ({query})"
            print(context)

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')
