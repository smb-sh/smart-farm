from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import request 
from django.shortcuts import render, redirect

@login_required(login_url='login')
def panel(request):
    
        

    context = {
        'hello':'hello my friend'
    }
    return render(request, 'main.html', context)

