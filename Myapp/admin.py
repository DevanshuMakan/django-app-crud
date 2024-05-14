from django.contrib import admin

from Myapp.models import *

# Register your models here.



class CourseAdmin(admin.ModelAdmin):
    list_display = ['Course_Name', 'Course_fee', 'Course_duration']
    search_fields = ['Course_Name','Course_fee']
    list_filter = ['Course_fee','Course_Name']
    ordering = ['Course_fee']
admin.site.register(Course, CourseAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Student_Name', 'Student_Mail', 'Student_course']
    search_fields = ['Student_Name','Student_course']
    list_filter = ['Student_course','Student_Name']
    ordering = ['Student_course']
admin.site.register(Student, StudentAdmin)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['Teacher_Name', 'Teacher_email']
    search_fields = ['Teacher_Name','Teacher_email']
    list_filter = ['Teacher_email','Teacher_Name']
    ordering = ['Teacher_email']
admin.site.register(Teacher, TeacherAdmin)


