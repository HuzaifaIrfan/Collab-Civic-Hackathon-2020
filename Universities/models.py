from django.db import models

# Create your models here.
# from allauth.socialaccount.models import SocialAccount
from django.utils.translation import gettext_lazy as _


class Universities(models.Model):
    name=models.CharField(max_length=20)
    full_name=models.CharField(max_length=100)

    image = models.ImageField(upload_to ='static/img/unis/')

    description=models.TextField()


    email_domain=models.CharField(max_length=100)

    domain_name=models.CharField(max_length=100)


    class Meta:
        verbose_name = _("University")
        verbose_name_plural = _("Universities")


    def __str__(self):
        return self.full_name




class Departments(models.Model):
    name=models.CharField(max_length=20)
    full_name=models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


    def __str__(self):
        return self.full_name




class Batches(models.Model):
    name=models.CharField(max_length=20)

    class Meta:
        verbose_name = _("Batch")
        verbose_name_plural = _("Batches")

    def __str__(self):
        return self.name
