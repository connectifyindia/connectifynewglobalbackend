from django.shortcuts import render
from Ainaw_And_Social_Connect.models import RegisterNGO, NonRegisterNGO, SocialActivist_Enterpreneur, Business_Manpower,Admin
from Ainaw_And_Social_Connect.serializer import RegisterNGOSerializer,NonRegisterNGOSerializer,SocialActivist_EnterpreneurSerializer,Business_ManpowerSerializer,RegisterNGOLoginSerializer,NonRegisterNGOLoginSerializer,SocialActivist_EnterpreneurLoginSerializer,Business_ManpowerLoginSerializer,AdminSerializer,AdminLoginSerializer
from rest_framework import generics
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status

class  RegisterNGOCreateView(generics.CreateAPIView):
    queryset = RegisterNGO.objects.all()
    serializer_class =  RegisterNGOSerializer

class  NonRegisterNGOCreateView(generics.CreateAPIView):
    queryset =  NonRegisterNGO.objects.all()
    serializer_class = NonRegisterNGOSerializer

class SocialActivistCreateView(generics.CreateAPIView):
    queryset = SocialActivist_Enterpreneur.objects.all()
    serializer_class = SocialActivist_EnterpreneurSerializer

class BusinessCreateView(generics.CreateAPIView):
    queryset = Business_Manpower.objects.all()
    serializer_class = Business_ManpowerSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class=AdminSerializer


# Create your views here.

@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def RegisterNGO_login_view(request):
    if request.method=="POST":
        serializer =RegisterNGOLoginSerializer(data=request.data)
        require_fields = {
            "email" : "email"
        }
        qs_fields_data = {}
        for k,v  in require_fields.items():
            qs_fields_data[v] = request.data.get(k)

        pwd = request.data.get('password')
        qs_fields_data['password'] = pwd

        # from django.conf import settings
        # password = make_password(pwd, salt=settings.SECRET_KEY)
        # qs_fields_data['password'] = password

        account_instance = RegisterNGO.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def NonRegisterNGO_login_view(request):
    if request.method=="POST":
        serializer =NonRegisterNGOLoginSerializer(data=request.data)
        require_fields = {
            "email" : "email"
        }
        qs_fields_data = {}
        for k,v  in require_fields.items():
            qs_fields_data[v] = request.data.get(k)

        pwd = request.data.get('password')
        qs_fields_data['password'] = pwd

        # from django.conf import settings
        # password = make_password(pwd, salt=settings.SECRET_KEY)
        # qs_fields_data['password'] = password

        account_instance = NonRegisterNGO.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def SocialActivist_Enterpreneur_login_view(request):
    if request.method=="POST":
        serializer =SocialActivist_EnterpreneurLoginSerializer(data=request.data)
        require_fields = {
            "email" : "email"
        }
        qs_fields_data = {}
        for k,v  in require_fields.items():
            qs_fields_data[v]=request.data.get(k)

        pwd = request.data.get('password')
        qs_fields_data['password'] = pwd

        # from django.conf import settings
        # password = make_password(pwd, salt=settings.SECRET_KEY)
        # qs_fields_data['password'] = password

        account_instance = SocialActivist_Enterpreneur.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Business_Manpower_login_view(request):
    if request.method=="POST":
        serializer =Business_ManpowerLoginSerializer(data=request.data)
        require_fields = {
            "email" : "email"
        }
        qs_fields_data = {}
        for k,v  in require_fields.items():
            qs_fields_data[v] = request.data.get(k)

        pwd = request.data.get('password')
        qs_fields_data['password'] = pwd

        # from django.conf import settings
        # password = make_password(pwd, salt=settings.SECRET_KEY)
        # qs_fields_data['password'] = password

        account_instance = Business_Manpower.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def Admin_login_view(request):
    if request.method=="POST":
        serializer =AdminLoginSerializer(data=request.data)
        require_fields = {
            "email" : "email"
        }
        qs_fields_data = {}
        for k,v  in require_fields.items():
            qs_fields_data[v] = request.data.get(k)

        pwd = request.data.get('password')
        qs_fields_data['password'] = pwd

        # from django.conf import settings
        # password = make_password(pwd, salt=settings.SECRET_KEY)
        # qs_fields_data['password'] = password

        account_instance = Admin.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
