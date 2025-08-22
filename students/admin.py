
from django.contrib import admin
from .models import Student, Enrollment


# Inline Enrollment so it shows inside Student Admin
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'get_status')
    search_fields = ('name',)
    inlines = [EnrollmentInline]

    # Custom column for enrollment status
    def get_status(self, obj):
        enrollments = obj.enrollments.all()
        if enrollments.exists():
            return ", ".join([enrollment.status for enrollment in enrollments])
        return "No Enrollment"
    get_status.short_description = 'Status'


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_name', 'status')
    list_filter = ('status',)
