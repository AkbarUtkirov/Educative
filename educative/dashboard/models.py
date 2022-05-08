from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    student = models.IntegerField()

    def __str__(self):
        return self.name


class Note(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.teacher.username

