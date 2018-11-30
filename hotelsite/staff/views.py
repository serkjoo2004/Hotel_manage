from django.shortcuts import render, get_object_or_404
from .models import Room
from django.shortcuts import render, redirect

def staff_home(request):
    rooms = Room.objects.order_by('room_num')
    return render(request, 'staff/staff_home.html', {'rooms':rooms})

def log_out(request):
    return redirect('/')