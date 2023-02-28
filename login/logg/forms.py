from django import forms
from . models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,User

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    Fname=forms.CharField(required=True)
    Lname=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    
    class Meta:
        model=User
        fields=['Fname','Lname','username','email','phone','password1','password2']
    
    def save(self,commit=True):
        user=super(UserRegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.Fname=self.cleaned_data['Fname']
        user.Lname=self.cleaned_data['Lname']
        if commit:
            user.save()
        return user 
        
