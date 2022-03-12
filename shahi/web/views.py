from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import StudentForms,EmployeeForms,TeacherForms,RegistationForms
# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
    form=StudentForms
    if request.method=='POST':
        stud_form=StudentForms(request.POST)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('/student')
    return render(request,'student.html',{'form':form})

def employee(request):
    form=EmployeeForms
    if request.method=='POST':
        emp_form=EmployeeForms(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/employee')
    return render(request,'employee.html',{'form':form})


def teacher(request):
    form=TeacherForms
    if request.method=='POST':
        teach_form=TeacherForms(request.POST)
        if teach_form.is_valid():
            teach_form.save()
            return redirect('/teacher')
    return render(request,'teacher.html',{'form':form})

def register(request):
    form=RegistationForms
    if request.method=='POST':
        reg_form=RegistationForms(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/register')
    return render(request,'register.html',{'form':form})
