from rest_framework import serializers
from apps.quiz.models import PythonQuestions


class SingleQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonQuestions
        fields = 'correct_option',
