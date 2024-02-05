from django.shortcuts import render
from Counsel_For_Academic_And_Job.models import Student, Trainer_Counsellor, Professional_Employee, ContentPublisher,Admin,Server,ConnectifyAdmin,ProjectLeader,ProjectManager,Content_Publisher
from Counsel_For_Academic_And_Job.serializer import StudentSerializer, TrainerSerializer, ProfessionalSerializer, ContentPublisherSerializer,AdminSerializer,StudentLoginSerializer,TrainerLoginSerializer,ProfessionalLoginSerializer,ContentPublisherLoginSerializer,AdminLoginSerializer,ServerLoginSerializer,ProjectLeaderLoginSerializer,ProjectLeaderSerializer,ProjectManagerSerializer,ProjectManagerLoginSerializer,ServerSerializer,Content_PublisherSerializer,Content_PublisherLoginSerializer,ConnectifyAdminSerializer,ConnectifyAdminLoginSerializer
from rest_framework import generics
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TrainerCreateView(generics.CreateAPIView):
    queryset = Trainer_Counsellor.objects.all()
    serializer_class = TrainerSerializer

class ProfessionalCreateView(generics.CreateAPIView):
    queryset = Professional_Employee.objects.all()
    serializer_class = ProfessionalSerializer

class ContentPublisherCreateView(generics.CreateAPIView):
    queryset = ContentPublisher.objects.all()
    serializer_class = ContentPublisherSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class=AdminSerializer


# Create your views here.
@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def Student_login_view(request):
    if request.method=="POST":
        serializer =StudentLoginSerializer(data=request.data)
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

        account_instance = Student.objects.filter(**qs_fields_data)
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
def Trainer_login_view(request):
    if request.method=="POST":
        serializer =TrainerLoginSerializer(data=request.data)
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

        account_instance = Trainer_Counsellor.objects.filter(**qs_fields_data)
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
def Professional_login_view(request):
    if request.method=="POST":
        serializer =ProfessionalLoginSerializer(data=request.data)
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

        account_instance = Professional_Employee.objects.filter(**qs_fields_data)
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
def ContentPublisher_login_view(request):
    if request.method=="POST":
        serializer =ContentPublisherLoginSerializer(data=request.data)
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

        account_instance = ContentPublisher.objects.filter(**qs_fields_data)
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
        
# VIEWS FOR CONNECTIFYINDIA

class ServerCreateView(generics.CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ProjectLeaderCreateView(generics.CreateAPIView):
    queryset = ProjectLeader.objects.all()
    serializer_class = ProjectLeaderSerializer

class ProjectManagerCreateView(generics.CreateAPIView):
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerSerializer

class Content_PublisherCreateView(generics.CreateAPIView):
    queryset = Content_Publisher.objects.all()
    serializer_class = Content_PublisherSerializer

class ConnectifyAdminCreateView(generics.CreateAPIView):
    queryset = ConnectifyAdmin.objects.all()
    serializer_class=ConnectifyAdminSerializer


# Create your views here.
@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def Server_login_view(request):
    if request.method=="POST":
        serializer =ServerLoginSerializer(data=request.data)
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

        account_instance = Server.objects.filter(**qs_fields_data)
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
def ProjectLeader_login_view(request):
    if request.method=="POST":
        serializer =ProjectLeaderLoginSerializer(data=request.data)
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

        account_instance =ProjectLeader.objects.filter(**qs_fields_data)
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
def ProjectManager_login_view(request):
    if request.method=="POST":
        serializer =ProjectManagerLoginSerializer(data=request.data)
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

        account_instance = ProjectManager.objects.filter(**qs_fields_data)
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
def Content_Publisher_login_view(request):
    if request.method=="POST":
        serializer =Content_PublisherLoginSerializer(data=request.data)
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

        account_instance = Content_Publisher.objects.filter(**qs_fields_data)
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
def ConnectifyAdmin_login_view(request):
    if request.method=="POST":
        serializer =ConnectifyAdminLoginSerializer(data=request.data)
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

        account_instance = ConnectifyAdmin.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
