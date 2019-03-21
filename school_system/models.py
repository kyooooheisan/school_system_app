from django.db import models
from django.utils import timezone

# Create your models here.
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
