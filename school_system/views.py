from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.db import models
from django.db.models import Sum
from school_system.forms import StudentForm,LessonRecordForm
from school_system.forms import StudentEditForm,LessonRecordEditForm
from school_system.models import Student,LessonRecord
import calendar
import datetime

PRICE_HOUR={'English':3500,'Programing':3500,'Finance':3300}


def top(request):
    return render(request, 'school_system/top.html',{})


def index(request):
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
            lesson=form.save(commit=False)
            lesson.price=lesson.lesson_time * PRICE_HOUR[lesson.genre]
            lesson.save()
            return HttpResponseRedirect(reverse('lessonrecord_index'))
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
            return HttpResponseRedirect(reverse('index'))
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
            lesson=form.save(commit=False)
            lesson.price=lesson.lesson_time * PRICE_HOUR[lesson.genre]
            lesson.save()
            return HttpResponseRedirect(reverse('lessonrecord_index'))
    else:
        form=LessonRecordEditForm(instance=lessonrecord)
    return TemplateResponse(request,'school_system/lessonrecord_edit.html',{'form':form,'lessonrecord':lessonrecord})



def invoice_list(request):

    return TemplateResponse(request,'school_system/invoice_list.html',{})

# #下記の方策は一旦pending
# def invoice_list(request):
#
#     invoice_data= LessonRecord.objects.all()
# #ジャンル一覧を取得
#     genre_list=[]
#     genre_data= LessonRecord.objects.all().order_by('-genre')
#
#     for genre in genre_data:
#         genre_list.append(genre.genre)
# #顧客一覧を取得
#     user_list=[]
#     user_data= LessonRecord.objects.all().order_by('-name')
#     for user in user_data:
#         user_list.append(user.name)
# #日付一覧を取得
#     date_list=[]
#     for i in genre_data:
#         date_list.append((i.date.strftime('%Y/%m/%d')[:7]))
#
#     unique_date_list=list(set(date_list))
#     unique_date_list.sort(reverse=False)
#
#
#     monthly_sum_data=[]
#     for i in range(len(unique_date_list)):
#         year,month=unique_date_list[i].split("/")
#         month_range= calendar.monthrange(int(year),int(month))[1]
#         first_date=year + "-" + month + "-" + "01"
#         last_date=year + "-" + month + "-" + str(month_range)
#
#         total_of_month=LessonRecord.objects.filter(date__range=(first_date,last_date))
#         genre_total=total_of_month.values('genre').annotate(total_price=Sum('price'))
#
#         for j in range(len(category_total)):
#             money= category_total[j]['total_price']
#
#
#     return TemplateResponse(request,'school_system/invoice_list.html',{})
