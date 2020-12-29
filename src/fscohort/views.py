from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from fscohort.models import Student


def home_view(request):
    # return HttpResponse("This is about page")
    
    # form = StudentForm()
    
    # my_context = {
    #     'title': '<b>Clarusway</b>',
    #     'dict_1': {'django':'best framework'},
    #     'my_list': [2, 3, 4, 5],
    #     'form': form
        
    # }
    return render(request, "fscohort/home.html")

def student_list(request):
    students = Student.objects.all()
    context ={
        'students': students
    }
    
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        'form': form
        
    }
    return render(request, "fscohort/student_add.html", context)

def student_detail(request, id):
    student = Student.objects.get(id=id)
    
    context = {
        'student': student
    }
    
    return render(request, "fscohort/student_detail.html", context)
    