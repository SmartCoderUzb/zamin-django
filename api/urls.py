from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from .views import *
from course.views import *

router = DefaultRouter()
router.register("category",CategoryViewSet)
router.register("course",CourseViewSet)
router.register("course-department",CourseDepartmentViewSet)
router.register("course-part",CoursePartViewSet)
router.register("news-category",NewsCategoryViewSet)
router.register("news",NewsViewSet)
router.register("users", UserViewset)
router.register('tests',TestViewset)
router.register('question',QuestionViewset)
router.register('choice',ChoiceViewset)

urlpatterns = [
    path("", include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
