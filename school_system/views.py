from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return render(request, 'school_system/index.html',{})
# Create your views here.
