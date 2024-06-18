from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated as IA
from rest_framework.authentication import BasicAuthentication

from .serializers import CourseCategorySerializer, CourseSerializer, CourseDepartmentSerializer, CoursePartSerializer, NewsCategorySerializer, NewsSerializer
from .serializers import *
from course.models import *


class IsAuthenticated(IA):
    def has_permission(self, request, view):
        # return True
        if request.method == "GET":
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class UserViewset(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    serializer_class = UserModelSerializer
    queryset = User.objects


class CategoryViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects

class CourseViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects

class CourseDepartmentViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CourseDepartmentSerializer
    queryset = CourseDepartment.objects

class CoursePartViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CoursePartSerializer
    queryset = CoursePart.objects

class NewsCategoryViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects

class NewsViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    queryset = News.objects


# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
