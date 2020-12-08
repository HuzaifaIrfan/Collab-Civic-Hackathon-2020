from __future__ import absolute_import

from django import forms

from allauth.account.forms import BaseSignupForm

from . import app_settings, signals
from .adapter import get_adapter
from .models import SocialAccount


class SignupForm(BaseSignupForm):
    def __init__(self, *args, **kwargs):
        self.sociallogin = kwargs.pop("sociallogin")
        initial = get_adapter().get_signup_form_initial_data(self.sociallogin)
        kwargs.update(
            {
                "initial": initial,
                "email_required": kwargs.get(
                    "email_required", app_settings.EMAIL_REQUIRED
                ),
            }
        )
        super(SignupForm, self).__init__(*args, **kwargs)

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.save_user(request, self.sociallogin, form=self)
        self.custom_signup(request, user)
        return user

    def validate_unique_email(self, value):
        try:
            return super(SignupForm, self).validate_unique_email(value)
        except forms.ValidationError:
            raise forms.ValidationError(
                get_adapter().error_messages["email_taken"]
                % self.sociallogin.account.get_provider().name
            )


class DisconnectForm(forms.Form):
    account = forms.ModelChoiceField(
        queryset=SocialAccount.objects.none(),
        widget=forms.RadioSelect,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        self.accounts = SocialAccount.objects.filter(user=self.request.user)
        super(DisconnectForm, self).__init__(*args, **kwargs)
        self.fields["account"].queryset = self.accounts

    def clean(self):
        cleaned_data = super(DisconnectForm, self).clean()
        account = cleaned_data.get("account")
        if account:
            get_adapter(self.request).validate_disconnect(account, self.accounts)
        return cleaned_data

    def save(self):
        account = self.cleaned_data["account"]
        account.delete()
        signals.social_account_removed.send(
            sender=SocialAccount, request=self.request, socialaccount=account
        )




import django
from django import forms
from django.contrib import admin

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
class edit_profile_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'edit_profile_form'
        self.helper.form_class = 'form-group text-center'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        # self.helper.label_class = 'hidden'

        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
        Field('university',label = "", css_class='form-control'),
        Field('department', css_class='form-control'),
        Field('batch', css_class='form-control'),
        Field('registration_number', css_class='form-control'),
        Field('bio', rows="3" , css_class='form-control md-textarea'),
        Field('contact', rows="3" , css_class='form-control md-textarea'),
    )



    class Meta:
        model = SocialAccount
        # filter_horizontal=('skills',)

        #remove university for final as it will be verified and added through email

        fields = ['university','department', 'batch','bio','contact','registration_number']

    # helper.layout = Layout(
    #     Field('title', css_class='form-control mt-2 mb-3'),
    #     Field('text', rows="3", css_class='form-control mb-3'),
    #     Field('author', css_class='form-control mb-3'),
    #     Field('tags', css_class='form-control mb-3'),
    #     Field('slug', css_class='form-control'),
    # )
