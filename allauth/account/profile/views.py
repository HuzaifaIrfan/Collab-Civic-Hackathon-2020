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



def profile(request):

    return render(request,'profile/profile.html')



def profile_edit(request):

    return render(request,'profile/profile.html')














