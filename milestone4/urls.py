"""milestone4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from threeauth.views import logout, login, registration, user_profile

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #3lite URLSs
    path('', include('threelite.urls')),
    #User Auth URLS
    path('auth/', include('threeauth.urls')),
    path('auth/logout/', logout, name="logout"),
    path('auth/login/', login, name="login"),
    path('auth/register', registration, name="registration"),
    path('auth/profile', user_profile, name="profile"),
    #passwordreset needs to be completed
    #path('auth/password-reset', include(url_reset)),
    #blogurls
    path('blog/', include('threeblog.urls'))
    
]
