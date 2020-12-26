from .forms import StudentForm
from .models import Student
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# Create your views here.


def index(request):
    # return HttpResponse('<h1>hello world!.</h1>')
    return render(request, 'fscohort/home.html')


def student_num(request):
    print(request.user)
    students = Student.objects.all()
    num_of_stdnt = Student.objects.count()
    context = {
        'students': students,
        'num': num_of_stdnt
    }
    # return HttpResponse("FS Cohort has {} students". format(num_of_stdnt))
    return render(request, 'fscohort/student_list.html', context)

# Add a student Creat student


def student_add(request):
    form = StudentForm()
    html = "Welcom"
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            html = "Student Succesfully added"
            # return HttpResponseRedirect(reverse('fscohort:student_num'))
            return redirect('fscohort:student_num')
    context = {
        'form': form,
        'html': html
    }
    return render(request, 'fscohort/student_add.html', context)

# Detail a student


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)

# Update a student


def student_update(request, id):
    obj = get_object_or_404(Student, id=id)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("fscohort:student_detail", id)
    context = {
        "student": obj,
        "form": form
    }
    return render(request, "fscohort/student_add.html", context)

#  Delete a student


def student_delete(request, id):
    # student = get_object_or_404(Student,id=id)
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('fscohort:student_num')

    return render(request, "fscohort/student_delete.html")
