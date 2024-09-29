from django.shortcuts import render,redirect
from user.models import * 
from django.core.files.storage import FileSystemStorage
import datetime
from django.views.decorators.cache import cache_control
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)

def teacherdash(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            stu_count=Student.objects.filter(sclass=teacher.tclass).count()
            sub_count=Subjects.objects.filter(classid=teacher.tclass).count()
            noti=Notification.objects.all()
            return render(request,"teacherdash.html",locals())
        
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)

def teacherlogout(request):
    try:
        if request.session['teacher']!=None:
            del request.session['teacher']
            return render('login')
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)

def teachersubjects(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            sub=Subjects.objects.filter(teacherid=teacher.id)
            return render(request,"teachersubjects.html",locals())
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)

def teacherprofile(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            t=Teacher.objects.get(email=teacherid)
            if request.method=="POST":
                pic=request.FILES['pic']
                fs=FileSystemStorage()
                filename = fs.save(pic.name,pic)
                t.pic=filename
                t.save()
                return redirect('teacherapp:teacherprofile')
            return render(request,"teacherprofile.html",{'t':t})
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)

def teacherattend(request):
    try:
        if request.session['teacher']!=None:
            teacherid=request.session['teacher']
            teacher=Teacher.objects.get(email=teacherid)
            students=Student.objects.filter(sclass=teacher.tclass)
            att=StudentAttendance.objects.filter(sclass=teacher.tclass)
            if request.method=="POST":
                studentid=request.POST['studentid']
                studentname=request.POST['studentname']
                sclass=request.POST['sclass']
                d=datetime.datetime.today()
                date=d.strftime("%d-%m-%y")
                status=request.POST['status']
                try:
                    obj=StudentAttendance.objects.get(studentid=studentid,date=date)
                except ObjectDoesNotExist:
                    stu=StudentAttendance(studentid=studentid,sclass=sclass,date=date,status=status,studentname=studentname)
                    stu.save()
                    return redirect('teacherapp:teacherattend')
            return render(request,"teacherattend.html",locals())
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def delattend(request,id):
    try:
        if request.session['username']!=None:
            StudentAttendance.objects.get(id=id).delete()
            return redirect('teacherapp:teacherattend')
    except:
        return redirect('login')