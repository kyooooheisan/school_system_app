from django.db import models
from django.utils import timezone
from datetime import datetime,date
#参照：https://www.freelance-geek.com/w/2019/02/06/django-form-validation/
from django.core.validators import MaxValueValidator,MinValueValidator
#from django.core.validators import MaxLengthValidator,MinLengthValidator
import datetime
# Create your models here.
#生徒モデル
class Student(models.Model):

    GENDER_CHOICES=(
    ('male','男性'),
    ('female','女性')
    )
    name= models.CharField(verbose_name='名前',max_length=20,null=False,blank=False)
    gender= models.CharField(verbose_name='性別',max_length=10, choices=GENDER_CHOICES,default='male',null=False,blank=False)
    age= models.PositiveIntegerField(verbose_name="年齢",default=0)

    def __str__(self):
        return self.name


#受講記録モデル
class LessonRecord(models.Model):

    GENRE_CHOICES=(
    ('English','英語',),
    ('Programing','プログラミング',),
    ('Finance','ファイナンス',),
    )

    name= models.ForeignKey(Student,verbose_name='受講者',max_length=20,null=False,blank=False,on_delete=models.CASCADE)
    genre= models.CharField(verbose_name='ジャンル',choices=GENRE_CHOICES,max_length=10)
    lesson_day=models.DateField(verbose_name='受講日')
    lesson_time=models.PositiveIntegerField(verbose_name='受講時間',validators=[MaxValueValidator(12),MinValueValidator(1)])
    price=models.PositiveIntegerField(verbose_name='支払金額',null=True,blank=True)

    def __str__(self):
        return str(self.name)
