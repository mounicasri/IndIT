from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee



def index(request):
    return HttpResponse("Something went wrong!!!")


def employeesList(request):
    employees = Employee.objects.all()
    return render(request,"employees.html",{"employees":employees})
  #  return render(request, 'index.html', {'products': products})

