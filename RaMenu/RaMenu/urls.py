"""
URL configuration for RaMenu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from user_app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.main, name='index'),
    path('user/', include('user_app.urls')),
    path('desires/', include('desire_app.urls')),
    path('surveys/', include('survey_app.urls')),
    #path('draft/', include('draft.urls')),
    #path('', include('menu.urls')),
    #path('log/', include('user_app.urls')),
]
