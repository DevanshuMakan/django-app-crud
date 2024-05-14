from django.forms import ModelForm
from django import forms
from Myapp.models import *


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
class updatecourseform(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

