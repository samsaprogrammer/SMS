from django.shortcuts import render,redirect,reverse
import datetime
from user.models import*
from django.views.decorators.cache import cache_control
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def index(request):
    try:
        if request.session['username']!=None:
            stu_count=Student.objects.all().count()
            t_count=Teacher.objects.all().count()
            class_count=Class.objects.all().count()
            sub_count=Subjects.objects.all().count()
            t_noti=Notification.objects.all()
            return render(request,'adminhome.html',locals())
    except:
        return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def teacher(request):
    try:
        if request.session['username']!=None:
            if request.method=="POST":
                name=request.POST['name']
                number=request.POST['number']
                email=request.POST['email']
                qualification=request.POST['qualification']
                experience=request.POST['experience']
                tsalary=request.POST['tsalary']
                tclass=request.POST['tclass']
                address=request.POST['address']
                password=request.POST['password']
                created=datetime.datetime.today()
                try:
                    ob=Teacher.objects.get(email=email)
                    if ob is not None:
                        msg="Email is already registered"
                        t=Teacher.objects.all()
                        cl=Class.objects.all()
                        return render(request,'teacher.html',locals())
                except ObjectDoesNotExist:
                        teacher=Teacher(name=name,phone=number,email=email,qualification=qualification,experience=experience,tsalary=tsalary,tclass=tclass,address=address,created=created)
                        log=LoginUser(username=email,password=password,usertype="teacher")
                        teacher.save()
                        log.save()
                        t=Teacher.objects.all()
                        cl=Class.objects.all()
                        return redirect('adminapp:teacher')
            t=Teacher.objects.all().order_by('-created')
            cl=Class.objects.all() 
            return render(request,'teacher.html',{'t':t,'cl':cl})
    except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def student(request):
    try:
        if request.session['username']!=None:
            if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                email=request.POST['email']
                dob=request.POST['dob']
                mobile=request.POST['mobile']
                fnumber=request.POST['fnumber']
                sclass=request.POST['sclass']
                sfee=request.POST['sfee']
                balance=request.POST['balance']
                address=request.POST['address']
                password=request.POST['password']
                try:
                    ob=Student.objects.get(email=email)
                    if ob is not None:
                        msg="Email is already registered"
                        stu=Student.objects.all()
                        cl=Class.objects.all()
                        return render(request,'student.html',locals())
                except ObjectDoesNotExist:
                        stu=Student(name=name,fname=fname,mobile=mobile,email=email,fnumber=fnumber,dob=dob,sclass=sclass,sfee=sfee,balance=balance,address=address)
                        stu.save()
                        log=LoginUser(username=email,password=password,usertype="student")
                        log.save()
                        stu=Student.objects.all()
                        msg="Student is added successfully"
                        cl=Class.objects.all()
                        return render(request,'student.html',{'msg':"student is added",'stu':stu,'cl':cl})
            stu=Student.objects.all()
            cl=Class.objects.all()
            return render(request,'student.html',{'stu':stu,'cl':cl})
    except:
        return(redirect('login'))


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def classes(request):
    #try:
        if request.session['username']!=None:
            c=Class.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                roomno=request.POST['roomno']
                seats=request.POST['seats']
                c=Class(name=name,roomno=roomno,seats=seats)
                c.save()
                return redirect('adminapp:classes')
            return render(request,'classes.html',locals())
    #except:
            return(redirect('login'))

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def subjects(request):
    #try:
        if request.session['username']!=None:
            cl=Class.objects.all()
            sub=Subjects.objects.all()
            teacher=Teacher.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                classid=request.POST['classid']
                teacherid=request.POST['teacherid']
                book=request.POST['book']
                s=Subjects(name=name,classid=classid,teacherid=teacherid,book=book)
                s.save()
                return redirect('adminapp:subjects')

            return render(request,'subjects.html',locals())
    #except:
            #return(redirect('login'))

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def delsubject(request,id):
     try:
          if request.session['username']!=None:
               Subjects.objects.get(id=id).delete()
               return redirect('adminapp:subjects')
     except:
          return redirect('login')



@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def logout(request):
    try:
        if request.session['username']!=None:
            del request.session['username']
            return redirect('login')
    except:
        return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def delteacher(request,id):
    try:
        if request.session['username']!=None:
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:teacher')
    except:
        return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def delstudent(request,id):
    try:
        if request.session['username']!=None:
            Student.objects.get(id=id).delete()
            return redirect('adminapp:student')
    except:
        return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def editstudent(request,id):
    try:
        if request.session['username']!=None:
           stu=Student.objects.get(id=id)
           cl=Class.objects.all()
           if request.method=="POST":
                name=request.POST['name']
                fname=request.POST['fname']
                email=request.POST['email']
                dob=request.POST['dob']
                mobile=request.POST['mobile']
                fnumber=request.POST['fnumber']
                sclass=request.POST['sclass']
                sfee=request.POST['sfee']
                balance=request.POST['balance']
                address=request.POST['address']
                Student.objects.filter(id=id).update(name=name,fname=fname,mobile=mobile,email=email,dob=dob,fnumber=fnumber,sclass=sclass,sfee=sfee,balance=balance,address=address)
                return redirect('adminapp:student')
           

           return render(request,"editstudent.html",{'stu':stu,'cl':cl})
    except:
        return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def editteacher(request,id):
    #try:
        if request.session['username']!=None:
           t=Teacher.objects.get(id=id)
           if request.method=="POST":
                name=request.POST['name']
                phone=request.POST['phone']
                email=request.POST['email']
                qualification=request.POST['qualification']
                experience=request.POST['experience']
                tclass=request.POST['tclass']
                tsalary=request.POST['tsalary']
                address=request.POST['address']
                Teacher.objects.filter(id=id).update(name=name,phone=phone,email=email,qualification=qualification,experience=experience,tclass=tclass,tsalary=tsalary,address=address)
                return redirect('adminapp:teacher')
           

           return render(request,"editteacher.html",{'t':t})
    #except:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def editclass(request,id):
     try:
          if request.session['username']!=None:
               c=Class.objects.get(id=id)
               if request.method=="POST":
                    name=request.POST['name']
                    roomno=request.POST['roomno']
                    seats=request.POST['seats']
                    
                    Class.objects.filter(id=id).update(name=name,roomno=roomno,seats=seats)
                    return redirect('adminapp:classes')
               return render(request,"editclass.html",{'c':c})
     except:
          return redirect('login')
     

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def editsubject(request,id):
    # try:
          if request.session['username']!=None:
               sub=Subjects.objects.get(id=id)
               if request.method=="POST":
                    name=request.POST['name']
                    classid=request.POST['classid']
                    teacherid=request.POST['teacherid']
                    book=request.POST['book']
                    
                    Subjects.objects.filter(id=id).update(name=name,classid=classid,teacherid=teacherid,book=book)
                    return redirect('adminapp:subjects')
               return render(request,"editsubject.html",{'sub':sub})
     #except:
          #return redirect('login')
     
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewenquiry(request):
      try:
          if request.session['username']!=None:
               enq=Enquiry.objects.all()
               return render(request,'viewenquiry.html',locals())
      except:
           return redirect('login')
      
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def admincp(request):
     # try:
          if request.session['username']!=None:
               adminid=request.session['username']
               if request.method=="POST":
                    oldpassword=request.POST['oldpassword']
                    newpassword=request.POST['oldpassword']
                    cpassword=request.POST['cpassword']
                    try:
                         obj=LoginUser.objects.get(username=adminid,password=oldpassword)
                         if newpassword!=cpassword:
                              msg="Enter same password"
                         elif oldpassword==obj.password:
                              LoginUser.objects.filter(username=adminid,password=oldpassword).update(password=newpassword)
                              return redirect('adminapp:logout')
                    except:
                         return render(request,'admincp.html',{'msg':"Invalid Password"})
              
               return render(request,'admincp.html',locals())
      #except:
           #return redirect('login')


@cache_control(no_store=True,no_cache=True,must_revalidate=True)     
def notice(request):
     if request.method=="POST":
          notice=request.POST['notice']
          created=datetime.datetime.today()
          noti=Notification(notice=notice,created=created)
          noti.save()
          t_noti=Notification.objects.all()
          
          return redirect('adminapp:dash')
     return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)

def delattend(request,id):
     try:
          if request.session['username']!=None:
               Notification.objects.get(id=id).delete()
               return redirect('adminapp:dash')
     except:
          return redirect('login')



