from django.db import models

# Create your models here.


from Universities.models import Universities,Departments,Batches

from django.contrib.auth.models import User


from django.utils.translation import gettext_lazy as _

from  allauth.socialaccount.models import SocialAccount

from extras.extras import ContentTypeRestrictedFileField

class Project(models.Model):
    full_name = models.CharField(max_length=100,)


    social_user = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)

    university= models.ForeignKey(Universities, on_delete=models.SET_NULL, null=True,blank=True)

    description=models.TextField()
    image=models.ImageField(upload_to ='static/project/img',default='static/img/default_project.jpg')


    report= models.FileField(upload_to ='static/project/report', null=True,blank=True)

    # file = ContentTypeRestrictedFileField(
    #     upload_to='static/project/reports',
    #     content_types=['application/pdf', 'application/zip'],
    #     max_upload_size=5242880
    # )

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    # git_link = models.CharField(max_length=200,)

    
    # developed=models.BooleanField(default=True)

    # work_needed=models.BooleanField(default=False)




    def __str__(self):
        return self.full_name



# class Assigned_Project(models.Model):
#     full_name = models.CharField(max_length=100,)


#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     university= models.ForeignKey(Universities, on_delete=models.SET_NULL, null=True,blank=True)

#     description=models.TextField()
#     project_template=models.FileField(upload_to ='static/project/',null=True,blank=True)

    # git_link = models.CharField(max_length=200,)

    
    # developed=models.BooleanField(default=True)

    # work_needed=models.BooleanField(default=False)




    # def __str__(self):
    #     return self.full_name

