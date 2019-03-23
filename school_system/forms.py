from django import forms
from .models import Student,LessonRecord

class StudentForm(forms.ModelForm):

    class Meta:
        model= Student
        fields=('name','gender','age')

class StudentEditForm(forms.ModelForm):
    class Meta:
        model= Student
        fields=('name','gender','age')

class LessonRecordForm(forms.ModelForm):
    class Meta:
        model= LessonRecord
        fields=('name','genre','lesson_day','lesson_time')

class LessonRecordEditForm(forms.ModelForm):
    class Meta:
        model= LessonRecord
        fields=('name','genre','lesson_day','lesson_time')
