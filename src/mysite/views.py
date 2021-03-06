from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import request 
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate ,logout
from .forms import LoginForm
from decription_app.models import MyData
from Adafruit_IO import Client, Feed, Data, RequestError



@login_required(login_url='login/')
def panel(request):
    
    # my_data = MyData.objects.filter(user=request.user.id).last()
    
    #new version 
    ADAFRUIT_IO_KEY = 'hello world'

    ADAFRUIT_IO_USERNAME = 'smart_farm'
    aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    
    humidity = aio.feeds('humidity')
    moisture = aio.feeds('moisture')
    temperature = aio.feeds('temperature')
    rain = aio.feeds('rain')
    uv = aio.feeds('uv')
    


    humidity_data = aio.receive_previous(humidity.key)
    moisture_data = aio.receive_previous(moisture.key)
    temperature_data = aio.receive_previous(temperature.key)
    rain_data = aio.receive_previous(rain.key)
    uv_data = aio.receive_previous(uv.key)
    # print(humidity_data,
    # moisture_data,
    # pump_data,
    # temperature_data,
    # rain_data,
    # uv_data
    # )
    if humidity_data.value == 'nan':
        my_humidity = 0
    else:
        my_humidity = humidity_data.value

    if temperature_data.value == 'nan':
        my_temper = 0
    else:
        my_temper = temperature_data.value
    context = {
        'humidity':my_humidity,
        'moisture':moisture_data.value,
        'temperature':my_temper,
        'rain':rain_data.value,
        'uv':uv_data.value,
        'date_added':uv_data.created_at
        
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
            login_form.add_error('user_name', '???????????? ???? ???????????? ???????? ?????? ???????? ??????')

    context = {
        'login_form': login_form
    }
    return render(request, 'hallway.html', context)



def log_out(request):
    
    logout(request)
           
    return redirect('/')