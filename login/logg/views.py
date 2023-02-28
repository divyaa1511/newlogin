from django.shortcuts import redirect,render
from . forms import *
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'logg/index.html')



def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            
            username=form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!!")
            return redirect("index")
    else:
        form=UserRegistrationForm()
    context={
        'form':form,
    }
    return render(request,"logg/register.html",context)

