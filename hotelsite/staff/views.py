from django.shortcuts import render

def staff_home(request):
    return render(request, 'staff/staff_home.html')
# Create your views here.
