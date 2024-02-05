from rest_framework import serializers
from Project_Youth_And_Business_Enterpreneur_Network.models import Organisation, Intern_JobkeerStudent, Startup, Consultant,Admin


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        organisation = Organisation.objects.create(
            fullName=validated_data['fullName'],    
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        organisation.save()
        return organisation


class Intern_JobkeerStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern_JobkeerStudent
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        intern = Intern_JobkeerStudent.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        intern.save()
        return intern


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        startup = Startup.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        startup.save()
        return startup


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        consultant = Consultant.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        consultant.save()
        return consultant
    
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
    
class OrganisationLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Organisation
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Organisation.objects.filter(email=email,password=password).exists():
            return True
        return False

class Intern_JobkeerStudentLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Intern_JobkeerStudent
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Intern_JobkeerStudent.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class StartupLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Startup
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Startup.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class ConsultantLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Consultant
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Consultant.objects.filter(email=email,password=password).exists():
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
