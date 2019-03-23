from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse

from school_system.forms import StudentForm
from school_system.forms import StudentEditForm
from school_system.models import Student




def top(request):
    return render(request, 'school_system/top.html',{})

def index(request):
    """メイン画面"""
    students= Student.objects.all()
    return render(request,'school_system/index.html',{'students':students,})


def student_create(request):
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form=StudentForm()

    return TemplateResponse(request, 'school_system/student_create.html',{'form':form})


def student_edit(request,student_id):
    try:
        student=Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form= StudentEditForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student_edit',args=(student.id,)))
    else:
        form=StudentEditForm(instance=student)
    return TemplateResponse(request,'school_system/student_edit.html',{'form':form, 'student':student})



# Create your views here.
