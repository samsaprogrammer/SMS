from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('dash',views.index,name="dash"),
    path('teacher',views.teacher,name="teacher"),
    path('student',views.student,name="student"),
    
    path('classes',views.classes,name="classes"),
    path('subjects',views.subjects,name="subjects"),
    path('logout',views.logout,name="logout"),
    path('delteacher/<id>',views.delteacher,name="delteacher"),
    path('delstudent/<id>',views.delstudent,name="delstudent"),
    path('delsubject/<id>',views.delsubject,name="delsubject"),
    path('editstudent/<id>',views.editstudent,name="editstudent"),
    path('editteacher<id>',views.editteacher,name="editteacher"),
    path('editsubject/<id>',views.editsubject,name="editsubject"),
    path('editclass<id>',views.editclass,name="editclass"),
    path('viewenquiry/',views.viewenquiry,name="viewenquiry"),
    path('admincp/',views.admincp,name="admincp"),
    path('notice/',views.notice,name="notice"),
    path('delattend/<id>',views.delattend,name="delattend"),

    

    



    
]