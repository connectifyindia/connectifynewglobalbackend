from django.db import models

# Create your models here.


class Organisation(models.Model):
    # sub_project_choices = [
    #     ('Organisation/Firm/Franchise','Organisation/Firm/Franchise'),
    #     ('Intern/Jokeer Student','Intern/Jokeer Student'),
    #     ('Startup/Interpreneur','Startup/Interpreneur'),
    #     ('Consultant/BDM','Consultant/BDM'),
    # ]
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
class Intern_JobkeerStudent(models.Model):
    # sub_project_choices = [
    #     ('Organisation/Firm/Franchise', 'Organisation/Firm/Franchise'),
    #     ('Intern/Jokeer Student', 'Intern/Jokeer Student'),
    #     ('Startup/Interpreneur', 'Startup/Interpreneur'),
    #     ('Consultant/BDM', 'Consultant/BDM'),
    # ]
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
class Startup(models.Model):
    # sub_project_choices = [
    #     ('Organisation/Firm/Franchise', 'Organisation/Firm/Franchise'),
    #     ('Intern/Jokeer Student', 'Intern/Jokeer Student'),
    #     ('Startup/Interpreneur', 'Startup/Interpreneur'),
    #     ('Consultant/BDM', 'Consultant/BDM'),
    # ]
    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Consultant(models.Model):
    # sub_project_choices = [
    #     ('Organisation/Firm/Franchise', 'Organisation/Firm/Franchise'),
    #     ('Intern/Jokeer Student', 'Intern/Jokeer Student'),
    #     ('Startup/Interpreneur', 'Startup/Interpreneur'),
    #     ('Consultant/BDM', 'Consultant/BDM'),
    # ]

    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
    
class Admin(models.Model):
    # sub_project_choices = [
    #     ('student/parents', 'student/parents'),
    #     ('trainer/counsellor', 'trainer/counsellor'),
    #     ('professional/employee', 'professional/employee'),
    #     ('content publisher', 'content publisher'),
    # ]

    fullName = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
