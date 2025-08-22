

# Register your models here.
from django.contrib import admin
from .models import Student, Enrollment

admin.site.register(Student)
admin.site.register(Enrollment)
