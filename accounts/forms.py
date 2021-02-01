from django.contrib.auth.forms import UserCreationForm
from accounts.models import User,Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class Signupform(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password should be same" ,code= "invalid")

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)