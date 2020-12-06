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


def profile(request):

    return render(request,'profile/profile.html')



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











