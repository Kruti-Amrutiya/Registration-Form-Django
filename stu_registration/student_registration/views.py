from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.views import View


# Create your class based views here.
# Class to show the list of students
class StudentListView(View):
    def get(self, request):
        context = {'student_list': Student.objects.all()}
        return render(request, "student_register/student_list.html", context)


# Class to register any student
class StudentFormView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, "student_register/student_form.html", {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            dob = form.cleaned_data['dob']
            roll_num = form.cleaned_data['roll_num']
            gender = form.cleaned_data['gender']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            reg = Student(fullname=fullname, dob=dob, roll_num=roll_num, gender=gender, mobile=mobile, email=email, subject=subject)
            reg.save()
        return HttpResponseRedirect('/student/list')


# Class to update any student data
class StudentUpdateView(View):
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, "student_register/student_form.html", {'form': form})

    def post(self, request, id):
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/student/list')


# Class to delete any student from student list
class StudentDeleteView(View):
    def post(self, request, id):
        student = Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect('/student/list')

# Create your functional views here.
# Function to show the list of students
'''def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "student_register/student_list.html", context)


# Function to register any student
def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            dob = form.cleaned_data['dob']
            roll_num = form.cleaned_data['roll_num']
            gender = form.cleaned_data['gender']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            reg = Student(fullname=fullname, dob=dob, roll_num=roll_num, gender=gender, mobile=mobile, email=email, subject=subject)
            reg.save()
            form = StudentForm()
        return redirect('student/list')
    else:
        form = StudentForm()
    return render(request, "student_register/student_form.html", {'form': form})


# Function to update any student data
def student_update(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, "student_register/student_form.html", {'form': form})


# Function to delete any student from student list
def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')'''
