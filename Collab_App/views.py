from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User




def home_view(request):

    # users=User.objects.all()
    # for user in users:
    #     print(user.id)
    #     socialaccounts=user.socialaccount_set.all()
    #     for socialaccount in socialaccounts:
    #         print(socialaccount.extra_data['name'])


    return render(request,'Home.html')


def about_view(request):


    return render(request,'About.html')




def contact_view(request):


    return render(request,'Contact.html')

