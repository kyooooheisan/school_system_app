from django.shortcuts import render
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from school_system.forms import StudentForm
from school_system.models import Student



def top(request):
    return render(request, 'school_system/top.html',{})

def index(request):
    """メイン画面"""
    students= Student.objects.all()
    return render(request,'school_system/index.html',{'students':students,})


def create_student(request):
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=StudentForm()

    return render(request, 'school_system/create_student.html',{'form':form})



# Create your views here.
