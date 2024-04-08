from django.db import models

# Create your models here.
class StudentClass(models.Model):
    class_name = models.CharField(max_length=155)
    section = models.CharField(max_length=5)
    def __str__(self):
        return self.class_name
    
class Student(models.Model):
    stuname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class_name = models.ForeignKey(StudentClass,on_delete=models.CASCADE, related_name='student_class')
    
    def __str__(self):
        return self.stuname
    