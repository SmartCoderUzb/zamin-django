from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication

from .models import *
from .serializers import *


class TestViewset(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    serializer_class = TestModelSerializer
    queryset = Test.objects

class QuestionViewset(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    serializer_class = QuestionModelSerializer
    queryset = Question.objects

class ChoiceViewset(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    serializer_class = ChoiceModelSerializer
    queryset = Choice.objects