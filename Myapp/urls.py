from django.urls import path

from Myapp.views import *

urlpatterns =[
    path('', home, name = 'home'),
    path('Student', student, name = 'student'),
    path('Teacher', teacher, name='teacher'),
    path('Course', course, name = 'course'),
    path('create_student', create_student, name = 'create_student'),
    path('create_teacher', create_teacher, name = 'create_teacher'),
    path('create_course', create_course, name = 'create_course'),
    path('update_course/<int:pk>/', updateCourse, name = 'update course'),
    path('delete_course/<int:pk>/', delete_course, name = 'delete course'),
    path('update_student/<int:pk>/', update_student, name = 'update student'),
    path('delete_student/<int:pk>/', delete_student, name = 'delete student'),
    path('update_teacher/<int:pk>/', update_teacher, name = 'update teacher'),
    path('delete_teacher/<int:pk>/', delete_teacher, name = 'delete teacher'),


]