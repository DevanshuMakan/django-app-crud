from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *

from Myapp.forms import *
from Myapp.models import *

def home(request):
    return render(request, 'base.html')

def student(request):
    stud = Student.objects.all()
    return render(request, 'student.html', {'stud': stud})
def teacher(request):
    teach = Teacher.objects.all()
    return render(request, 'teacher.html', {'teach': teach})
def course(request):
    course1 = Course.objects.all()
    return render(request, 'course.html', {'course1': course1})
def create_student(request):
    courses = Course.objects.all()

    if request.method =='POST':
        stu_name = request.POST['student_name']
        stu_email = request.POST['email']
        course = request.POST['course']
        print(stu_email,stu_name,course)
        Student.objects.create(Student_Name=stu_name,Student_Mail=stu_email,Student_course_id=course)
        return redirect('/Student')
    else:
        return render(request, 'create_student.html', {'courses': courses})
def create_teacher(request):
    if request.method == 'POST':
        trainer_name = request.POST['teacher_name']
        trainer_email = request.POST['teacher_email']
        course = request.POST.getlist('course')
        trainer = Teacher.objects.create(Teacher_Name=trainer_name,Teacher_email=trainer_email)
        # trainer.trainer_course.set(course)
        # for c in course:
        #     trainer.trainer_course.add(c)
        trainer.Course_Taught.add(*course)
        trainer.save()

        return redirect('/Teacher')
    else:
        courses = Course.objects.all()
        return render(request,'create_teacher.html',{'courses':courses})

def create_course(request):
    courses = Course.objects.all()
    if request.method =='POST':
        course_name = request.POST['course_name']
        course_fee = request.POST['course_fee']
        course_duration = request.POST['course_duration']
        print(course_name,course_fee,course_duration)
        Course.objects.create(Course_Name=course_name,Course_fee=course_fee,Course_duration=course_duration)
        return redirect('/Course')
    else:
        return render(request, 'create_course.html', {'courses': courses})

def updateCourse(request,pk):
    course1 = Course.objects.get(pk=pk)
    form = CourseForm(instance=course1)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course1)
        if form.is_valid():
            form.save()
            return redirect('/Course')
        else:
            return render(request,'update_course.html',{'form': form})
    return render(request, 'update_course.html',{'form': form})


def delete_course(request,pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('/Course')

def delete_student(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/Student')

def delete_teacher(request,pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()
    return redirect('/Teacher')
def update_student(request,pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/Student')
        else:
            return render(request,'update_student.html',{'form': form})
    return render(request, 'update_student.html',{'form': form})
def update_teacher(request,pk):
    teach = Teacher.objects.get(pk=pk)
    form = TeacherForm(instance=teach)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teach)
        if form.is_valid():
            form.save()
            return redirect('/Teacher')
        else:
            return render(request,'update_teacher.html',{'form': form})
    return render(request, 'update_teacher.html',{'form': form})