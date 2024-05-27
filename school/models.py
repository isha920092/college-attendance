from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^/[0-9]/', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=10)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('B.sc. cs','B.sc. cs'),('M.sc. cs','M.sc. cs'),('M.sc. ca','M.sc. ca')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.PositiveIntegerField(max_length=10)
    mobile = models.CharField(max_length=10,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
   date=models.DateField(auto_now=True)
   by=models.CharField(max_length=20,null=True,default='school')
   message=models.CharField(max_length=500)

class Count(models.Model):
    d=models.DateField()
    c=models.CharField(max_length=10)
    c_p=models.IntegerField(default=0)
    c_a=models.IntegerField(default=0)
