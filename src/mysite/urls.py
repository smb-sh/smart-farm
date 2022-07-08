"""smart farm URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include
from .views import panel ,login_page ,log_out
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',panel,name='panel'),
    path('login/',login_page, name='login'),
    path('logout/',log_out, name='logout'),
    path('api/',include('api_app.urls')),
    # path('account/',include('account_app.urls')),
    # path('header', header, name="header"),
    # path('footer', footer, name="footer"),
    # path('email/',include('email_app.urls')),
    # path('pass/',include('password_app.urls')),
]
