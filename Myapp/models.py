from django.db import models


# Create your models here.
from django.db import models

# Create your models here.
class Course(models.Model):
    Course_Name = models.CharField(max_length=255)
    Course_fee = models.IntegerField(null=True)
    Course_duration = models.IntegerField(null=True)

    def __str__(self):
        return self.Course_Name

class Student(models.Model):
    Student_Name = models.CharField(max_length=255)
    Student_Mail = models.CharField(max_length=255, null=True)
    Student_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Student_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Student_Name

class Teacher(models.Model):
    Teacher_Name = models.CharField(max_length=255)
    Teacher_email = models.CharField(max_length=255, null=True)
    Course_Taught = models.ManyToManyField(Course)

    def __str__(self):
        return self.Teacher_Name