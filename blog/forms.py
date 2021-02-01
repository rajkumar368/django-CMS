from django import forms
from django.forms import ModelForm
from blog.models import post
from accounts.models import User
from tinymce.widgets import TinyMCE

class Contactform(forms.Form):
    countries = [("IN","INDIA"),("USA","AMERICA")]
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    email = forms.EmailField(required=False)
    phone = forms.RegexField(regex="^[6-9][0-9]{9}$",required=False)
    massage = forms.CharField(max_length=500)
    country = forms.ChoiceField(choices=countries) 

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        if email == '' and phone == '':
            raise forms.ValidationError("Atleast email or phone number should be provided" ,code= "invalid")

class Postform(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 18, 'rows': 10}))
    author = forms.CharField(disabled=True)
    class Meta:
        model = post
        fields = ["title","content","status","category","image","date",]


class Searchform(forms.Form):
    search = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'special','placeholder':'search'}))
    
    # def clean_image(self):
    #     image = self.cleaned_data.get('image')
    #     if image.size > 200000:
    #         raise forms.ValidationError('use low size image', code="invalid")
    #     else:
    #         return image
