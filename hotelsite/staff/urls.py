from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('', views.staff_home, name='staff_home'),
    path('login', views.log_out, name="logout"),
]