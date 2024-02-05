from rest_framework import serializers
from Counsel_For_Academic_And_Job.models import Student,Trainer_Counsellor,Professional_Employee,ContentPublisher,Admin,Server,ProjectLeader,ProjectManager,ConnectifyAdmin,Content_Publisher
from django.contrib.auth.hashers import make_password



class StudentSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields = ('student_name', 'email', 'mobile', 'password')

    def create(self,validated_data):
        student=Student.objects.create(
            student_name=validated_data['student_name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # password=make_password(validated_data['password']),
        )
        student.save()
        return student
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer_Counsellor
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        trainer=Trainer_Counsellor.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],  
        mobile=validated_data['mobile'],
        password=validated_data['password'],

        # password=make_password(validated_data['password']),
        # subproject=validated_data['subproject']
        )
        trainer.save()
        return trainer

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professional_Employee
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        professional=Professional_Employee.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=validated_data['password'],

        # password=make_password(validated_data['password']),
        # subproject=validated_data['subproject']
        )
        professional.save()
        return professional

class ContentPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContentPublisher
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        content=ContentPublisher.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=validated_data['password'],

        # password=make_password(validated_data['password']),
         # subproject=validated_data['subproject']
        )
        content.save()
        return content

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        admin=Admin.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=validated_data['password'],

        # password=make_password(validated_data['password']),
         # subproject=validated_data['subproject']
        )
        admin.save()
        return admin


class StudentLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Student
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Student.objects.filter(email=email,password=password).exists():
            return True
        return False

class TrainerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Trainer_Counsellor
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Trainer_Counsellor.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class ProfessionalLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Professional_Employee
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Professional_Employee.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class ContentPublisherLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =ContentPublisher
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if ContentPublisher.objects.filter(email=email,password=password).exists():
            return True
        return False

class AdminLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Admin
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Admin.objects.filter(email=email,password=password).exists():
            return True
        return False



# SERIALIZER FOR CONNECTIFYINDIA

class ServerSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = Server
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self,validated_data):
        server=Server.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # password=make_password(validated_data['password']),
        )
        server.save()
        return server

class ProjectLeaderSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = ProjectLeader
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self,validated_data):
        projectleader=ProjectLeader.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # password=make_password(validated_data['password']),
        )
        projectleader.save()
        return projectleader
    

class ProjectManagerSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = ProjectManager
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self,validated_data):
        projectmanager=ProjectManager.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # password=make_password(validated_data['password']),
        )
        projectmanager.save()
        return projectmanager

class ConnectifyAdminSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model =ConnectifyAdmin
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self,validated_data):
        admin=ConnectifyAdmin.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # password=make_password(validated_data['password']),
        )
        admin.save()
        return admin
    
class Content_PublisherSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model =Content_Publisher
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self,validated_data):
        content=Content_Publisher.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # password=make_password(validated_data['password']),
        )
        content.save()
        return content  



class ServerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Server
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Server.objects.filter(email=email,password=password).exists():
            return True
        return False  
    
class ProjectLeaderLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =ProjectLeader
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if ProjectLeader.objects.filter(email=email,password=password).exists():
            return True
        return False  
    
class ProjectManagerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =ProjectManager
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if ProjectManager.objects.filter(email=email,password=password).exists():
            return True
        return False  

class ConnectifyAdminLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =ConnectifyAdmin
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if ConnectifyAdmin.objects.filter(email=email,password=password).exists():
            return True
        return False  
    
class Content_PublisherLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Content_Publisher
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Content_Publisher.objects.filter(email=email,password=password).exists():
            return True
        return False  
    