from django.db import models

# Create your models here.

class College(models.Model):
    college_id = models.IntegerField(primary_key=True)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name
    
class Student(models.Model):
    college_id = models.ForeignKey(College,on_delete=models.CASCADE)
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    student_dept = models.CharField(max_length=100)
    student_phno = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
    
