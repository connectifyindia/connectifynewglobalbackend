
from django.shortcuts import render
from .models import Admin,BusinessDeveloper,Consumer,Manager,Publisher,Blog,VideoTestimonial,SuccessStory,Document,Carreer,BootcampAcount,Bootcamp,Doc,FeedBack
from .serializer import AdminSerializer,BusinessDeveloperSerializer,ConsumerSerializer,ManagerSerializer,PublisherSerializer,AdminLoginSerializer,BusinessDeveloperLoginSerializer,ConsumerLoginSerializer,ManagerLoginSerializer,PublisherLoginSerializer,BlogSerializer,VideoTestimonialSerializer,SuccessStorySerializer,DocumentSerializer,CarreerSerializer,BootcampAcountSerializer,BootcampSerializer,DocSerializer,FormSerializer,FormSerializer1,FormSerializer2,FormSerializer3,FormSerializer4,FormSerializer5,FormSerializer6,FormSerializer7,FeedBackSerializer
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# from .pagination import EmployeePagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

class PublisherCreateView(generics.CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ManagerCreateView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class =ManagerSerializer

class ConsumerCreateView(generics.CreateAPIView):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

class BusinessDeveloperCreateView(generics.CreateAPIView):
    queryset = BusinessDeveloper.objects.all()
    serializer_class = BusinessDeveloperSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def Publisher_login_view(request):
    if request.method=="POST":
        serializer =PublisherLoginSerializer(data=request.data)
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

        account_instance = Publisher.objects.filter(**qs_fields_data)
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
def Manager_login_view(request):
    if request.method=="POST":
        serializer =ManagerLoginSerializer(data=request.data)
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

        account_instance = Manager.objects.filter(**qs_fields_data)
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
        serializer =ConsumerLoginSerializer(data=request.data)
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

        account_instance = Consumer.objects.filter(**qs_fields_data)
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
def BusinessDeveloper_login_view(request):
    if request.method=="POST":
        serializer =BusinessDeveloperLoginSerializer(data=request.data)
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

        account_instance = BusinessDeveloper.objects.filter(**qs_fields_data)
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

class BlogListView(generics.ListCreateAPIView):
     queryset=Blog.objects.all()
     serializer_class=BlogSerializer
     filter_backends=[DjangoFilterBackend]
     filterset_fields=['category']
     pagination_class=PageNumberPagination

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'

class DocListView(generics.ListCreateAPIView):
     queryset=Doc.objects.all()
     serializer_class=DocSerializer
     filter_backends=[DjangoFilterBackend]
     filterset_fields=['category']
     pagination_class=PageNumberPagination

class MyDocDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    lookup_field = 'slug'

class TestimonialVideoListView(generics.ListCreateAPIView):
     queryset=VideoTestimonial.objects.all()
     serializer_class=VideoTestimonialSerializer
     pagination_class=PageNumberPagination

class SuccessStoryListView(generics.ListCreateAPIView):
     queryset=SuccessStory.objects.all()
     serializer_class=SuccessStorySerializer
     pagination_class=PageNumberPagination

class SuccessStoryDetailView(generics.RetrieveUpdateDestroyAPIView):
      queryset=SuccessStory.objects.all()
      serializer_class=SuccessStorySerializer
      lookup_field = 'slug'

class DocumentListView(generics.ListCreateAPIView):
     queryset=Document.objects.all()
     serializer_class=DocumentSerializer
     filter_backends=[DjangoFilterBackend]  
     filterset_fields=['category','sub_category']
     pagination_class=PageNumberPagination

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Document.objects.all()
     serializer_class=DocumentSerializer
     lookup_field ='slug'

from rest_framework.parsers import MultiPartParser,FormParser
class CarreerCreateView(generics.CreateAPIView):
     parser_classes=(MultiPartParser,FormParser)
     queryset=Carreer.objects.all()
     serializer_class=CarreerSerializer

class BootcampRegistrationView(generics.ListCreateAPIView):
    queryset=BootcampAcount.objects.all()
    serializer_class=BootcampAcountSerializer

class BootcampListView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser,)
    queryset=Bootcamp.objects.all()
    serializer_class=BootcampSerializer

class BootcampDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bootcamp.objects.all()
    serializer_class=BootcampSerializer
    lookup_field = 'slug'

class FormAPIView(APIView):
    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)
class FormAPIView1(APIView):
    def post(self, request):
        serializer = FormSerializer1(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)

class FormAPIView2(APIView):
    def post(self, request):
        serializer = FormSerializer2(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class FormAPIView3(APIView):
    def post(self, request):
        serializer = FormSerializer3(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class FormAPIView4(APIView):
    def post(self, request):
        serializer = FormSerializer4(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class FormAPIView5(APIView):
    def post(self, request):
        serializer = FormSerializer5(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)

class FormAPIView6(APIView):
    def post(self, request):
        serializer = FormSerializer6(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)

class FormAPIView7(APIView):
    def post(self, request):
        serializer = FormSerializer7(data=request.data)
        if serializer.is_valid():
            # Handle valid form data
            return Response(serializer.validated_data, status=201)
        else:
            return Response(serializer.errors, status=400)

class FeedBackAPIView(generics.CreateAPIView):
    queryset=FeedBack.objects.all()
    serializer_class=FeedBackSerializer
    