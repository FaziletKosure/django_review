from .forms import StudentForm
from .models import Student
from django.http import HttpResponseRedirect
from django.shortcuts import render
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


def student_add(request):
    form = StudentForm()
    html = "Welcom"
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            html = "Student Succesfully added"
            return HttpResponseRedirect(reverse('fscohort:student_num'))
    context = {
        'form': form,
        'html': html
    }
    return render(request, 'fscohort/student_add.html', context)
