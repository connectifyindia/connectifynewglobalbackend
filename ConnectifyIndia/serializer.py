from .models import Admin,BusinessDeveloper,Consumer,Manager,Publisher,Blog,Doc,VideoTestimonial,SuccessStory,Document,Carreer,BootcampAcount,Bootcamp,FormModel,FormModel1,FormModel2,FormModel3,FormModel4,FormModel5,FormModel6,FormModel7,FeedBack
from rest_framework import serializers

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('fullname', 'email', 'mobile', 'password')

    def create(self, validated_data):
        publisher = Publisher.objects.create(
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],  
        )
        publisher.save()
        return publisher


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('fullname', 'email', 'mobile', 'password')

    def create(self, validated_data):
        manager = Manager.objects.create(
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
        )
        manager.save()
        return manager


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('fullname', 'email', 'mobile', 'password')

    def create(self, validated_data):
        consumer = Consumer.objects.create(
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
        )
        consumer.save()
        return  consumer


class BusinessDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDeveloper
        fields = ('fullname', 'email', 'mobile', 'password')

    def create(self, validated_data):
        businessdeveloper = BusinessDeveloper.objects.create(
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
        )
        businessdeveloper.save()
        return businessdeveloper
    
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('fullname', 'email', 'mobile', 'password')

    def create(self, validated_data):
        admin = Admin.objects.create(
            fullname=validated_data['fullname'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
        )
        admin.save()
        return admin
    
class PublisherLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Publisher
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Publisher.objects.filter(email=email,password=password).exists():
            return True
        return False

class ManagerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Manager
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Manager.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class ConsumerLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Consumer
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Consumer.objects.filter(email=email,password=password).exists():
            return True
        return False
    
class BusinessDeveloperLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =BusinessDeveloper
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if BusinessDeveloper.objects.filter(email=email,password=password).exists():
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
    
from django.utils.html import strip_tags
class BlogSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    def create(self, validated_data):
        validated_data['content'] = strip_tags(validated_data['content'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['content'] = strip_tags(validated_data['content'])
        return super().update(instance, validated_data)
    class Meta:
        model=Blog
        fields='__all__'

from .models import Doc
class DocSerializer(serializers.ModelSerializer):
     def create(self, validated_data):
        validated_data['content'] = strip_tags(validated_data['content'])
        return super().create(validated_data)

     def update(self, instance, validated_data):
        validated_data['content'] = strip_tags(validated_data['content'])
        return super().update(instance, validated_data)
     class Meta:
        model=Doc
        fields='__all__'

from .models import VideoTestimonial
class VideoTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoTestimonial
        fields=['title','image_url','name','description','video']

from .models import SuccessStory
class SuccessStorySerializer(serializers.ModelSerializer):
     def create(self, validated_data):
        validated_data['content'] = strip_tags(validated_data['content'])
        return super().create(validated_data)

     def update(self, instance, validated_data):
        validated_data['content'] = strip_tags(validated_data['content'])
        return super().update(instance, validated_data)
     
     class Meta:
        model=SuccessStory
        fields='__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=['id','slug','title','image_url','category','sub_category','document']
        
class CarreerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carreer
        fields='__all__'

class BootcampAcountSerializer(serializers.ModelSerializer):
    class Meta:
        model=BootcampAcount
        fields="__all__"

class BootcampSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bootcamp
        fields='__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model=FormModel
        fields='__all__'

class FormSerializer1(serializers.ModelSerializer):
    class Meta:
        model=FormModel1
        fields='__all__'

class FormSerializer2(serializers.ModelSerializer):
    class Meta:
        model=FormModel2
        fields='__all__'

class FormSerializer3(serializers.ModelSerializer):
    class Meta:
        model=FormModel3
        fields='__all__'

class FormSerializer4(serializers.ModelSerializer):
    class Meta:
        model=FormModel4
        fields='__all__'

class FormSerializer5(serializers.ModelSerializer):
    class Meta:
        model=FormModel5
        fields='__all__'

class FormSerializer6(serializers.ModelSerializer):
    class Meta:
        model=FormModel6
        fields='__all__'

class FormSerializer7(serializers.ModelSerializer):
    class Meta:
        model=FormModel7
        fields='__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields='__all__'