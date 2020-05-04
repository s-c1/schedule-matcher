from django.conf import settings
from django.db import models
from django.utils import timezone 

class Course(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_code = models.TextField()
    course_time = models.DateTimeField()
    course_prof = models.TextField()
    student = Student()

    def enter(self):
        self.course_code = input("(e.g. CMPUT 204) Course code:")
        self.course_time = input("(e.g. Thursday, Friday, 9 - 10 AM) When the course take place:")
        self.course_prof = input("(First, Last name) Who teaches the course:")
        self.save()
    
    def match():
        
    
    def __str__(self):
        return self.course_code

class Student(models.Model):
    name = models.TextField()
    email = models.TextField()
    course_list = [Course()]

    

def match(list_student:List):
    for i, j in list_student:
        for k in course_list:

