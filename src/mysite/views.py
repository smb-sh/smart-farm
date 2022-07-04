from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import request 
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate
from .forms import LoginForm
from decription_app.models import MyData

@login_required(login_url='login/')
def panel(request):
    
    my_data = MyData.objects.filter(user=request.user.id).last()
    

    context = {
        'mydata':my_data
        
    }
    return render(request, 'main.html', context)

def login_page(request):

    context ={
        'hello':'login page'
    }

    return render(request, 'hallway.html', context)

def login_page(request):
    if request.user.is_authenticated :
        # redirect to password panel
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }
    return render(request, 'hallway.html', context)