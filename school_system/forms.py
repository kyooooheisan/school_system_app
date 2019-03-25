from django import forms
from .models import Student,LessonRecord

CHOICES=(
("","選択肢から選んでください"),
("2019年3月","2019年3月"),
("2019年2月","2019年2月"),
("2019年1月","2019年1月"),
)

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

class PullDownForm(forms.Form):
    pulldown= forms.ChoiceField(widget=forms.Select,choices=CHOICES,label="プルダウンメニュー")
