from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User




def home_view(request):

    context={}

    # users=User.objects.all()
    # for user in users:
    #     print(user.id)
    #     socialaccounts=user.socialaccount_set.all()
    #     for socialaccount in socialaccounts:
    #         print(socialaccount.extra_data['name'])


    return render(request,'Home.html',context)


def about_view(request):

    context={}


    # context['page_title']='About'


    return render(request,'About.html',context)




def team_view(request):
    context={}

    # context['page_title']='Our Team'

    return render(request,'Team.html',context)

