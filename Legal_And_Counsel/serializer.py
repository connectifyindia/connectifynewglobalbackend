from rest_framework import serializers
from .models import Student_Intern, Advocate_Lawyer, Consumer_User, Content_PublishingUpload,User,Admin

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields='__all__'

class Student_InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Intern
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        student = Student_Intern.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']   

        )
        student.save()
        return student


class Advocate_LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate_Lawyer
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        advocate = Advocate_Lawyer.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        advocate.save()
        return advocate


class Consumer_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer_User
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        consumer = Consumer_User.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        consumer.save()
        return  consumer


class Content_PublishingUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content_PublishingUpload
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        content = Content_PublishingUpload.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        content.save()
        return content
    
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        admin = Admin.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        admin.save()
        return admin

class StudentLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Student_Intern
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Student_Intern.objects.filter(email=email,password=password).exists():
            return True
        return False

class Advocate_LawyerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Advocate_Lawyer
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Advocate_Lawyer.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class Consumer_UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Consumer_User
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Consumer_User.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class Content_PublishingUploadLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Content_PublishingUpload
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Content_PublishingUpload.objects.filter(email=email,password=password).exists():
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
    