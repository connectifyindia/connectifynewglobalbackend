from django.shortcuts import render
from .models import Student_Intern, Advocate_Lawyer, Consumer_User, Content_PublishingUpload,Admin
from .serializer import Student_InternSerializer, Advocate_LawyerSerializer, Consumer_UserSerializer,Content_PublishingUploadSerializer,AdminSerializer,StudentLoginSerializer,Advocate_LawyerLoginSerializer,Consumer_UserLoginSerializer,Content_PublishingUploadLoginSerializer,AdminLoginSerializer
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import EmployeePagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Student_InternCreateView(generics.CreateAPIView):
    queryset = Student_Intern.objects.all()
    serializer_class = Student_InternSerializer

class Advocate_LawyerCreateView(generics.CreateAPIView):
    queryset = Advocate_Lawyer.objects.all()
    serializer_class = Advocate_LawyerSerializer

class Consumer_UserCreateView(generics.CreateAPIView):
    queryset = Consumer_User.objects.all()
    serializer_class = Consumer_UserSerializer

class Content_ManagerCreateView(generics.CreateAPIView):
    queryset = Content_PublishingUpload.objects.all()
    serializer_class = Content_PublishingUploadSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


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

        account_instance = Student_Intern.objects.filter(**qs_fields_data)
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
def Advocate_login_view(request):
    if request.method=="POST":
        serializer =Advocate_LawyerLoginSerializer(data=request.data)
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

        account_instance = Advocate_Lawyer.objects.filter(**qs_fields_data)
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
def Consumer_login_view(request):
    if request.method=="POST":
        serializer =Consumer_UserLoginSerializer(data=request.data)
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

        account_instance = Consumer_User.objects.filter(**qs_fields_data)
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
        serializer =Content_PublishingUploadLoginSerializer(data=request.data)
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

        account_instance = Content_PublishingUpload.objects.filter(**qs_fields_data)
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
        


# Api class Start from here

# for Non Id Based
# class BlogListView(APIView):
#      pagination_class=PageNumberPagination

#      def get(self,request):
#           emp=Blog.objects.all().order_by("-id")
#           serializer=BlogSerializer(emp,many=True)
#           return Response(serializer.data)
     
#      def post(self,request):
#           postdata=request.data
#           print(postdata)
#           serializer=BlogSerializer(data=postdata)
#           if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data,status=status.HTTP_201_CREATED)
#           else:
#                return Response(serializer.errors,status=status.HTTP_405_METHOD_NOT_ALLOWED)

# # for Id based
# class BlogDetailView(APIView):
#      def get(self,request,id):
#          try:
#             emp=Blog.objects.get(id=id)
#          except Blog.DoesNotExist:
#           return Response("requested Resources not available")
#          else:
#           serializer=BlogSerializer(emp)
#           return Response(serializer.data)
#      def get_for_all_id(self,id):
#            try:
#           #   emp=Blog.objects.get(eno=id).latest('id')
#             emp=Blog.objects.get(id=id)


              
#            except Blog.DoesNotExist:
#             emp=None
#            return emp
#      def put(self,request,id):
#           print(request.data)
#           emp=self.get_for_all_id(id)
#           if emp is None:
#                return  Response('requested object not availabale',status=status.HTTP_404_NOT_FOUND)
#           else:
#                print(request.data)
#                serializer=BlogSerializer(emp,data=request.data)
#                if serializer.is_valid():
#                     serializer.save()
#                     return Response("data is updatated",status=status.HTTP_200_OK)
#                else:
#                     Response('data not available',status=status.HTTP_201_CREATED)
         
#      def delete(self,request,id):
#           try:
#             emp=Blog.objects.get(id=id)
#             emp.delete()
#             return Response("requested id  is deleted successfully",status=status.HTTP_204_NO_CONTENT)
#           except Blog.DoesNotExist:
#             return Response('requested object not avaible',status=status.HTTP_400_BAD_REQUEST)
