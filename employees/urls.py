from . import views
from django.urls import path

urlpatterns = [
    path('',views.employeesList),
    path('empInfo/',views.employeesList)
]