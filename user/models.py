from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    fname=models.CharField(max_length=25)
    mobile=models.CharField(max_length=13)
    email=models.CharField(max_length=30,unique=True)
    fnumber=models.CharField(max_length=11)
    dob=models.CharField(max_length=20)
    sclass=models.CharField(max_length=5)
    sfee=models.CharField(max_length=10)
    balance=models.IntegerField()
    pic=models.FileField(upload_to="")
    address=models.TextField()

class Teacher(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    email=models.CharField(max_length=25,unique=True)
    address=models.TextField()
    qualification=models.CharField(max_length=40)
    experience=models.CharField(max_length=40)
    tclass=models.CharField(max_length=20)
    tsalary=models.IntegerField()
    pic=models.FileField(upload_to="")
    created=models.DateTimeField()

class LoginUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=10)
    usertype=models.CharField(max_length=20)

class Class(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=25)
    roomno=models.CharField(max_length=20)
    seats=models.IntegerField()

class Subjects(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=25)
    classid=models.CharField(max_length=20)
    teacherid=models.CharField(max_length=20)
    book=models.FileField()

class StudentAttendance(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.CharField(max_length=10)
    studentname=models.CharField(max_length=50,default="")
    sclass=models.CharField(max_length=20,default="")
    date=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    enquiry_date=models.CharField(max_length=25)

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    notice=models.TextField()
    created=models.CharField(max_length=25)








