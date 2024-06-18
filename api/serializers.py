from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_framework import fields

from course.models import CourseCategory, Course, CourseDepartment, CoursePart, NewsCategory, News
from users.models import User


class UserModelSerializer(ModelSerializer):
    username = fields.CharField(max_length=150, required=False)
    class Meta:
        model = User
        fields ="__all__"
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseCategorySerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = CourseCategory
        fields = "__all__"


class CourseDepartmentSerializer(ModelSerializer):
    class Meta:
        model = CourseDepartment
        fields = "__all__"

class CoursePartSerializer(ModelSerializer):
    class Meta:
        model = CoursePart
        fields = "__all__"

class NewsCategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"  


# serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_staff'] = user.is_staff
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Include additional user information in the response
        data['is_staff'] = self.user.is_staff
        return data
