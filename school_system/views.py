from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse

from school_system.forms import StudentForm,LessonRecordForm
from school_system.forms import StudentEditForm,LessonRecordEditForm
from school_system.models import Student,LessonRecord




def top(request):
    return render(request, 'school_system/top.html',{})

def index(request):
    """メイン画面"""
#ID順に並ぶようにする
    students= Student.objects.all()
    return render(request,'school_system/index.html',{'students':students,})


def lessonrecord_index(request):
    lessonrecords= LessonRecord.objects.all()
    return render(request,'school_system/lessonrecord_index.html',{'lessonrecords':lessonrecords})


def student_create(request):
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form=StudentForm()

    return TemplateResponse(request, 'school_system/student_create.html',{'form':form,})


def lessonrecord_create(request):
    if request.method == 'POST':
        form= LessonRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lessonrecord_index')
    else:
        form=LessonRecordForm()

    return TemplateResponse(request, 'school_system/lessonrecord_create.html',{'form':form,})



def student_edit(request,student_id):
    try:
        student=Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form= StudentEditForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/index'))
    else:
        form=StudentEditForm(instance=student)
    return TemplateResponse(request,'school_system/student_edit.html',{'form':form, 'student':student})


def lessonrecord_edit(request,lessonrecord_id):
    try:
        lessonrecord=LessonRecord.objects.get(id=lessonrecord_id)
    except LessonRecord.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form= LessonRecordEditForm(request.POST,instance=lessonrecord)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/lessonrecord_index'))
    else:
        form=LessonRecordEditForm(instance=lessonrecord)
    return TemplateResponse(request,'school_system/lessonrecord_edit.html',{'form':form,'lessonrecord':lessonrecord})


# Create your views here.
