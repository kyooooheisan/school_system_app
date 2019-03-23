"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
import school_system.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',school_system.views.top,name="top"),
    path("index/",school_system.views.index,name="index"),
    path("student_create/",school_system.views.student_create,name="student_create"),
    #path('student_create/',include('school_system.urls')),
    #path('students/<int:student_id>/student_edit/',include('school_system.urls')),
    path("students/<int:student_id>/student_edit/",school_system.views.student_edit,name="student_edit"),
]
