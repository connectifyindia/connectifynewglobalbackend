from django.db import models
from tinymce import models as tinymce_models

class Publisher(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.email
    
class Manager(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.email


class Consumer(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.email


class BusinessDeveloper(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.email

class Admin(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.email

class Blog(models.Model):
     blog_choices = [
        ('carrier','carrier'),
        ('legal','legal'),
        ('ngo','ngo'),
        ('project','project'),
        ]
     slug = models.SlugField(max_length=254,null=False,unique=True)
     image_url = models.ImageField(blank=True,null=True)
     title = models.CharField(max_length=254,default='')
     description=models.TextField(default=True)
     content = tinymce_models.HTMLField(null=True)
     date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
     category=models.CharField(max_length=254, choices=blog_choices,blank=True,null=True)
   
     def __str__(self):
        return self.title
     
class Doc(models.Model):
     Doc_choices = [
        ('simplycounsel','simplycounsel'),
        ('legalaspire','legalaspire'),
        ('ainaw','ainaw'),
        ('businessconnect','businessconnect'),
        ]
     title = models.CharField(max_length=254)
     slug = models.SlugField(max_length=254,null=False,unique=True)
     image_url = models.ImageField(blank=True,null=True)
     description=models.TextField(default=True)
     content = tinymce_models.HTMLField(null=True)
     date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
     category=models.CharField(max_length=254,choices=Doc_choices,blank=True,null=True)
    
     def __str__(self):
        return self.title

class VideoTestimonial(models.Model):
    title=models.CharField(max_length=254,blank=True,null=True)
    image_url = models.ImageField(blank=True,null=True)
    name=models.CharField(max_length=150,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    video=models.FileField(blank=True,null=True,default=True)


class SuccessStory(models.Model):
    slug = models.SlugField(max_length=254, null=False, unique=True)
    title=models.CharField(max_length=254,blank=True,null=True)
    image_url = models.ImageField(blank=True,null=True)
    description=models.TextField(default=True)
    content = tinymce_models.HTMLField(null=True)  
    date=models.DateTimeField(auto_now_add=True,blank=True,null=True)


class Document(models.Model):
    doc_category_choices = [
        ('career','career'),
        ('legal','legal'),
        ('ngo','ngo'),
        ('project','project'),
     ]
    doc_sub_category_choices = [
        ('word','word'),
        ('excell','excell'),
        ('powerpoint','powerpoint'),
        ('pdf','pdf'),
     ]
    slug = models.SlugField(max_length=254,null=False,unique=True)
    title=models.CharField(max_length=254,blank=True,null=True)
    image_url = models.ImageField(blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True,choices=doc_category_choices)
    sub_category=models.CharField(max_length=100,blank=True,null=True,choices=doc_sub_category_choices)
    document=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.title


class Carreer(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    region = models.CharField(max_length=254,default=True)
    mobile = models.BigIntegerField(unique=True)
    message=models.TextField(blank=True,null=True)
    resume=models.FileField(blank=True,null=True)


class BootcampAcount(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=254)
    country=models.CharField(max_length=254,default=True)
    mobile=models.BigIntegerField(unique=True)
    category=models.CharField(max_length=254)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.fullname
    
class Bootcamp(models.Model):
    slug = models.SlugField(max_length=254,null=False,unique=True)
    title=models.CharField(max_length=254)
    heading1=models.TextField(default=True,null=True)
    heading2=models.TextField(default=True,null=True)
    bootcamp_date_detail=models.TextField(default=True)
    bootcamp_time_detail=models.CharField(max_length=254)
    bootcamp_starting_date=models.CharField(max_length=254)
    background_image_url = models.ImageField(default=True)
    image_url1 = models.ImageField(default=True)
    image_url2 = models.ImageField(default=True)
    url = models.URLField(default=True)
    name1=models.CharField(max_length=150,default=True)
    name2=models.CharField(max_length=150,default=True)
    desination1=models.CharField(max_length=254,default=True)
    desination2=models.CharField(max_length=254,default=True)
    def __str__(self):
        return self.title
    
class FormModel(models.Model):
     questions = models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email
class FormModel1(models.Model):
     questions = models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email

class FormModel2(models.Model):
     questions = models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email
     
class FormModel3(models.Model):
     questions= models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email
     
class FormModel4(models.Model):
     questions= models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email
     
class FormModel5(models.Model):
     questions=models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email
    
class FormModel6(models.Model):
     questions= models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)
     def __str__(self):
        return self.email
     
class FormModel7(models.Model):
     questions= models.TextField()
     firstname=models.CharField(max_length=150,default=True)
     lastname=models.CharField(max_length=150,default=True)
     mobile = models.CharField(max_length=20,default=True)
     email = models.EmailField(unique=True, max_length=254)
     location=models.CharField(max_length=100,default=True)
     segment=models.TextField(default=True)

     def __str__(self):
        return self.email
     
class FeedBack(models.Model):
    fullname=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    description=models.TextField()



    











