from django.shortcuts import render,redirect
from .models import LoginUser,Enquiry
import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def vision(request):
    return render(request,'vision.html')

def school(request):
    return render(request,'school.html')

def founder(request):
    return render(request,'founder.html')

def chairman(request):
    return render(request,'chairman.html')

def login(request):
    return render(request,'login.html')

def principal(request):
    return render(request,'principal.html')

def transport(request):
    return render(request,'transport.html')

def schoolmanagement(request):
    return render(request,'schoolmanagement.html')

def medical(request):
    return render(request,'medical.html')

def academics(request):
    return render(request,'academics.html')

def procedure(request):
    return render(request,'procedure.html')

def prospectus(request):
    return render(request,'prospectus.html')

def rules(request):
    return render(request,'rules.html')

def fee(request):
    return render(request,'fee.html')

def smartclass(request):
    return render(request,'smartclass.html')

def news(request):
    return render(request,'news.html')

def gallery(request):
    return render(request,'gallery.html')

def career(request):
    return render(request,'career.html')

def logcode(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        usertype=request.POST['utype']
        try:
            user=LoginUser.objects.get(username=username,password=password,usertype=usertype)
            if user.usertype=="admin":
                 request.session['username']=username
                 return redirect('adminapp:dash')
            elif usertype=="student":
                request.session['student']=username
                return redirect('studentapp:studentdash')
            elif user.usertype=="teacher":
                request.session['teacher']=username
                return redirect('teacherapp:teacherdash')
                
           
        except:
            return redirect('login')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        d=datetime.datetime.today()
        enquiry_date=d.strftime("%d-%m-%Y %I:%M %p")
        enq=Enquiry(name=name,mobile=mobile,email=email,subject=subject,message=message,enquiry_date=enquiry_date)
        enq.save()
        return render(request,'index.html',{'msg':"Your Enquiry is submitted"})
    return render(request,'contact.html')