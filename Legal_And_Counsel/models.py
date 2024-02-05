from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     is_student=models.BooleanField(default=False)
#     is_advocate=models.BooleanField(default=False)
#     is_consumer=models.BooleanField(default=False)
#     is_contentpublisher=models.BooleanField(default=False)
#     is_admin=models.BooleanField(default=False)

class Student_Intern(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default=True)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
    
class Advocate_Lawyer(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default=True)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Consumer_User(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default=True)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Content_PublishingUpload(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default=True)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email

class Admin(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default=True)
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
