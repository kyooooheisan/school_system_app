from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Student

def top(request):
    return render(request, 'school_system/top.html',{})

def index(request):
    students= Student.objects.all()
    return render(request,'school_system/index.html',{'students':students})
# Create your views here.
