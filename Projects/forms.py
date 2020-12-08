import django
from django import forms
from django.contrib import admin

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field,Reset

from .models import Project


class add_project_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'edit_profile_form'
        self.helper.form_class = 'form-group text-center'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        # self.helper.label_class = 'hidden'

        self.helper.add_input(Submit('submit', 'Add Project'))


        self.helper.layout = Layout(
        Field('full_name',label = "", css_class='form-control'),
        Field('assigned_project', css_class='form-control'),
        Field('image', css_class='form-control'),
                Field('git_link', css_class='form-control'),
        Field('youtube_link', css_class='form-control'),
        Field('report', css_class='form-control'),
        Field('description', rows="3" , css_class='form-control md-textarea'),
        Field('completed', css_class='form-control'),

        Field('info', rows="3" , css_class='form-control md-textarea'),
        Field('team', rows="3" , css_class='form-control md-textarea'),
    )



    class Meta:
        model = Project
        # filter_horizontal=('skills',)

        #remove university for final as it will be verified and added through email

        fields = ['full_name','assigned_project','description', 'image','report','git_link','youtube_link','info','team','completed']



class edit_project_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'edit_profile_form'
        self.helper.form_class = 'form-group text-center'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        # self.helper.label_class = 'hidden'

        self.helper.add_input(Submit('submit', 'Save Project'))

        self.helper.layout = Layout(
        Field('full_name',label = "", css_class='form-control'),
        Field('assigned_project', css_class='form-control'),
        Field('image', css_class='form-control'),
        Field('git_link', css_class='form-control'),
        Field('youtube_link', css_class='form-control'),
        Field('report', css_class='form-control'),
        Field('description', rows="3" , css_class='form-control md-textarea'),
                Field('completed', css_class='form-control'),

        Field('info', rows="3" , css_class='form-control md-textarea'),
        Field('team', rows="3" , css_class='form-control md-textarea'),
    )



    class Meta:
        model = Project
        # filter_horizontal=('skills',)

        #remove university for final as it will be verified and added through email

        fields = ['full_name','assigned_project','description', 'image','report','git_link','youtube_link','info','team','completed']
