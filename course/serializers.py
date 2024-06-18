from rest_framework.serializers import ModelSerializer

from .models import Test, Question, Choice


class TestModelSerializer(ModelSerializer):
    
    class Meta:
        model = Test
        fields = "__all__"

class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class ChoiceModelSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"
