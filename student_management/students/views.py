from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Enrollment

def student_list(request):
    search_name = request.GET.get('search_name', '')
    filter_status = request.GET.get('status_filter', '')
    
    enrollments = Enrollment.objects.all()
    
    if search_name:
        enrollments = enrollments.filter(student__name__icontains=search_name)
    if filter_status:
        enrollments = enrollments.filter(status=filter_status)
    
    return render(request, 'students/student_list.html', {
        'enrollments': enrollments,
        'search_name': search_name,
        'filter_status': filter_status
    })
