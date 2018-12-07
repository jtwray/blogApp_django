"""blogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    #127.0.0.1:8000
    path('', include('blog.urls')),
    path('account/', include('django.contrib.auth.urls')),
    #path(r'^accounts/login/$', auth_views.LoginView),
    #path(r'^accounts/logout/$', view=auth_views.LogoutView, name='logout', kwargs={'nextPage'='/'}),
]
