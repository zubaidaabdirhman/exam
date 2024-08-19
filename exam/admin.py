from django.contrib import admin
from .models import Semester,Faculty,Course,Student,Batch

# Register your models here.
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Batch)