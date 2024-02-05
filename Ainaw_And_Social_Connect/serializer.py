from rest_framework import serializers
from Ainaw_And_Social_Connect.models import RegisterNGO, NonRegisterNGO, SocialActivist_Enterpreneur, Business_Manpower,Admin


class RegisterNGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterNGO
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        ngo = RegisterNGO.objects.create(
            fullName=validated_data[' fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        ngo.save()
        return ngo


class NonRegisterNGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonRegisterNGO
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        non_ngo = NonRegisterNGO.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        non_ngo.save()
        return non_ngo


class SocialActivist_EnterpreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialActivist_Enterpreneur
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        socialactivist = SocialActivist_Enterpreneur.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            # subproject=validated_data['subproject']
        )
        socialactivist.save()
        return socialactivist


class Business_ManpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Manpower
        fields = ('fullName', 'email', 'mobile', 'password')

    def create(self, validated_data):
        business = Business_Manpower.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=validated_data['password'],
        # subproject=validated_data['subproject']
        )
        business.save()
        return business
    
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
      
class RegisterNGOLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =RegisterNGO
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if RegisterNGO.objects.filter(email=email,password=password).exists():
            return True
        return False

class NonRegisterNGOLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =NonRegisterNGO
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if NonRegisterNGO.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class SocialActivist_EnterpreneurLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =SocialActivist_Enterpreneur
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if SocialActivist_Enterpreneur.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class Business_ManpowerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Business_Manpower
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Business_Manpower.objects.filter(email=email,password=password).exists():
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
