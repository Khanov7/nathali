from django.forms import ModelForm
from django import forms
from .models import UserProfile
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserSignUpForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'birthday', 'profilePicture']



    def __init__(self):
        super(UserSignUpForm,self).__init__()
        # self.fields['first_name'].widget.attrs.update({'class':'form-group'})
        # self.fields['last_name'].widget.attrs.update({'class': 'form-group'})
        # self.fields['email'].widget.attrs.update({'class': 'form-group'})
        # self.fields['password'].widget.attrs.update({'class': 'form-group'})
        # self.fields['birthday'].widget.attrs.update({'class': 'form-group'})
        # self.fields['profilePicture'].widget.attrs.update({'class': 'form-group'})
        self.fields['first_name'].label = "First Name"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class AdminUserSignUpForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'birthday', 'profilePicture', 'is_staff', 'is_superuser', 'status']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class AdminUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'birthday', 'profilePicture', 'is_staff', 'is_superuser', 'status']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
