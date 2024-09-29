from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import LoginUser
from .models import Class
from .models import Subjects
from .models import StudentAttendance
from .models import Enquiry
from .models import Notification
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(LoginUser)
admin.site.register(Class)
admin.site.register(Subjects)
admin.site.register(StudentAttendance)
admin.site.register(Enquiry)
admin.site.register(Notification)
