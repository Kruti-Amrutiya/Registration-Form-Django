from django.db import models


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    category = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    fullname = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    roll_num = models.CharField(max_length=3)
    gender = models.CharField(max_length=200, null=True, choices=category)
    mobile = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
