from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('vision-mission', views.vision, name="vision"),
    path('about-school',views.school,name="school"),
    path('founder',views.founder,name="founder"),
    path('chairman',views.chairman,name="chairman"),
    path('login',views.login,name="login"),
    path('logcode',views.logcode,name="logcode"),
    path('principal',views.principal,name="principal"),
    path('transport',views.transport,name="transport"),
    path('schoolmanagement',views.schoolmanagement,name="schoolmanagement"),
    path('medical',views.medical,name="medical"),
    path('academics',views.academics,name="academics"),
    path('contact',views.contact,name="contact"),
    path('procedure',views.procedure,name="procedure"),
    path('prospectus',views.prospectus,name="prospectus"),
    path('rules',views.rules,name="rules"),
    path('fee',views.fee,name="fee"),
    path('smartclass',views.smartclass,name="smartclass"),
    path('gallery',views.gallery,name="gallery"),
    path('news',views.news,name="news"),
    path('career',views.career,name="career"),
]
    

