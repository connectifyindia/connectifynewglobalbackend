from django.shortcuts import render
from Project_Youth_And_Business_Enterpreneur_Network.models import Organisation, Intern_JobkeerStudent, Startup, Consultant,Admin
from Project_Youth_And_Business_Enterpreneur_Network.serializer import OrganisationSerializer,Intern_JobkeerStudentSerializer,StartupSerializer,ConsultantSerializer,AdminSerializer,OrganisationLoginSerializer,Intern_JobkeerStudentLoginSerializer,StartupLoginSerializer,ConsultantLoginSerializer,AdminLoginSerializer
from rest_framework import generics
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
 
class OrganisationCreateView(generics.CreateAPIView):
    queryset=Organisation.objects.all()
    serializer_class=OrganisationSerializer

class Intern_JobSeekerStudentCreateView(generics.CreateAPIView):
     queryset=Intern_JobkeerStudent.objects.all()
     serializer_class=Intern_JobkeerStudentSerializer

class StartupCreateView(generics.CreateAPIView):
     queryset=Startup.objects.all()
     serializer_class=StartupSerializer

class ConsultantCreateView(generics.CreateAPIView):
     queryset=Consultant.objects.all()
     serializer_class=ConsultantSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class=AdminSerializer
    

# Create your views here.

@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def Organisation_login_view(request):
    if request.method=="POST":
        serializer =OrganisationLoginSerializer(data=request.data)
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

        account_instance = Organisation.objects.filter(**qs_fields_data)
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
def Intern_JobSeekerStudent_login_view(request):
    if request.method=="POST":
        serializer =Intern_JobkeerStudentLoginSerializer(data=request.data)
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

        account_instance = Intern_JobkeerStudent.objects.filter(**qs_fields_data)
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
def Startup_login_view(request):
    if request.method=="POST":
        serializer =StartupLoginSerializer(data=request.data)
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

        account_instance = Startup.objects.filter(**qs_fields_data)
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
def Consultant_login_view(request):
    if request.method=="POST":
        serializer =ConsultantLoginSerializer(data=request.data)
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

        account_instance = Consultant.objects.filter(**qs_fields_data)
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
