from django.shortcuts import render,redirect
from user.models import*
from django.views.decorators.cache import cache_control
from django.core.files.storage import FileSystemStorage
# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def studentdash(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            sub_count=Subjects.objects.filter(classid=stu.sclass).count()
            noti=Notification.objects.all()
            return render(request,'studentdash.html',{'stu':stu,'sub_count':sub_count,'noti':noti})
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def studentprofile(request):
   # try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            if request.method=="POST":
                pic=request.FILES['pic']
                fs=FileSystemStorage()
                filename = fs.save(pic.name,pic)
                stu.pic = filename
                stu.save()
                return redirect('studentapp:studentprofile')
            return render(request,'studentprofile.html',locals())
   # except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def studentlogout(request):
    try:
        if request.session['student']!=None:
            del request.session['student']
            return redirect('login')
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def studentsubject(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            sub=Subjects.objects.filter(classid=stu.sclass)
            return render(request,'studentsubject.html',locals())
    except:
        return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def studentattend(request):
    try:
        if request.session['student']!=None:
            studentid=request.session['student']
            stu=Student.objects.get(email=studentid)
            att=StudentAttendance.objects.filter(studentid=stu.id)
            return render(request,'studentattend.html',{'stu':stu,'att':att})
    except:
        return redirect('login')