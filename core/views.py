from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from core.forms import DepartmentForm, SchoolForm
from core.models import Department, School

def index(request):
    return render(request, 'home.html')

def school_list(request):
    schools=School.objects.all()
    context={
        "schools":schools
    }

    return render(request,'school_list.html',context)

def create_school(request):
    form = SchoolForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return HttpResponseRedirect(reverse('core:school_list'))
    context={
        "form":form,
    }
    return render(request, 'create_school.html',context)

def department_list(request):
    departments=Department.objects.all()
    context={
        "departments":departments
    }

    return render(request,'department_list.html',context)

def create_department(request):
    form = DepartmentForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return HttpResponseRedirect(reverse('core:department_list'))
    context={
        "form":form,
    }
    return render(request, 'create_department.html',context)