from rest_framework import serializers
from .models import ConnectifyIndia,SimplyCounsel,LegalAspire,Ainaw,BusinessConnect,Instagram,Twiter,Linkedln,Telegram,Whatsapp,FacebookModel,FileUpload

class ConnectifyIndiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConnectifyIndia
        fields='__all__'

class SimplyCounselSerializer(serializers.ModelSerializer):
    class Meta:
        model=SimplyCounsel
        fields='__all__'

class LegalAspireSerializer(serializers.ModelSerializer):
    class Meta:
        model=LegalAspire
        fields='__all__'

class AinawSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ainaw
        fields='__all__'

class BusinessConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusinessConnect
        fields='__all__'

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Instagram
        fields='__all__'

class TwiterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Twiter
        fields='__all__'

class LinkedlnSerializer(serializers.ModelSerializer):
    class Meta:
        model=Linkedln
        fields='__all__'

class TelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Telegram
        fields='__all__'

class WhatsappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Whatsapp
        fields='__all__'

class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model=FacebookModel
        fields='__all__'
# from .models import FileUpload
class DictionaryItemSerializer(serializers.Serializer):
      access_token =serializers.CharField()
      page_id = serializers.IntegerField()
      name=serializers.CharField()
      label=serializers.CharField()

# class ListOfDictsSerializer(serializers.Serializer):
#     items = DictionaryItemSerializer(many=True)
class FileUploadSerializer(serializers.Serializer):
     description=serializers.CharField()
     upload =serializers.FileField()
     selectedOption=DictionaryItemSerializer(many=True)
    # class Meta:
    #     model=FileUpload
    #     fields='__all__'

    # def get_photo_url(self,obj):
    #     request=self.context.get('request')
    #     photo_url=obj.fingerprint.url
    #     return request.build.absolute.uri(photo_url)
    
    # def create(self, validated_data):
    #     return FileUpload.objects.create(**validated_data)