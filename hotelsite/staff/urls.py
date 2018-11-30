from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('', views.staff_home, name='staff_home'),
    path('../', views.log_out, name="logout"),
]