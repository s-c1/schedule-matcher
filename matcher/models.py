from django.conf import settings
from django.db import models
from django.utils import timezone 

class Course(models.Model):
    course_code = models.TextField()

    def enter(self):
        self.course_code = input("Please enter course code")
    
    def __str__(self):
        return self.course_code