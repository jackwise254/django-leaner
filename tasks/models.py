from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
class Teacher(models.Model):
    fname =models.CharField(verbose_name="First name", max_length=64)
    lname =models.CharField(verbose_name="Last name", max_length=64)
    email =models.CharField(verbose_name="email name", max_length=64)
    class_id =models.CharField(verbose_name="class name", max_length=64)

class Centers(models.Model):
    cname =models.CharField(verbose_name="Center name", max_length=64, choices=Status.choices)
    country =models.CharField(verbose_name="country name", max_length=64, choices=Status.choices)
    city =models.CharField(verbose_name="city name", max_length=64)
    sessions =models.CharField(verbose_name="class name", max_length=64)
    
class Classes(models.Model):
    username =models.CharField(verbose_name="User name", max_length=64, unique=True)
    class_id =models.CharField(verbose_name="class name", max_length=64)
    subject =models.CharField(verbose_name="subject name", max_length=64)
    class_teacher =models.CharField(verbose_name="class teacher", max_length=64)

class Parent(models.Model):
    fname =models.CharField(verbose_name="First name", max_length=64)
    lname =models.CharField(verbose_name="Last name", max_length=64)
    email =models.CharField(verbose_name="email name", max_length=64, unique=True)
    location =models.CharField(verbose_name="location", max_length=64)
    occupation =models.CharField(verbose_name="occupation", max_length=64)

class Student(models.Model):
    fname =models.CharField(verbose_name="First name", max_length=64)
    lname =models.CharField(verbose_name="Last name", max_length=64)
    parentEmail =models.CharField(verbose_name="email name", max_length=64)
    class_name =models.CharField(verbose_name="class name", max_length=64)
    reg_no =models.CharField(verbose_name="registration number", max_length=64)
    adm_year =models.CharField(verbose_name="adm_year", max_length=64)
    final_year =models.CharField(verbose_name="final_year", max_length=64)
    age =models.CharField(verbose_name="age", max_length=64)
    gender =models.CharField(verbose_name="gender", max_length=64)
    location =models.CharField(verbose_name="location", max_length=64)

class Users(models.Model):
    fname =models.CharField(verbose_name="First name", max_length=64)
    lname =models.CharField(verbose_name="Last name", max_length=64)
    email =models.CharField(verbose_name="email name", max_length=64, unique=True)
    role =models.CharField(verbose_name="role", max_length=64)
    password =models.CharField(verbose_name="password", max_length=64)
    username =models.CharField(verbose_name="user name", max_length=64, unique=True)
    location =models.CharField(verbose_name="location", max_length=64)

    