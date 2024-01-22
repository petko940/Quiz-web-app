import random

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.quiz.models import PythonQuestions
from apps.quiz.api.serializers import SingleQuestionSerializer, PythonQuestionsSerializer, GetRightAnswerSerializer


class SingleQuestionAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            # TODO: add dbs
            question = PythonQuestions.objects.get(pk=pk)
        except PythonQuestions.DoesNotExist:
            question = None

        if question:
            serializer = SingleQuestionSerializer(question)
            return Response(serializer.data)

        return Response()


# ----------------------------------
class GetRightAnswerAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            # TODO: add dbs
            question = PythonQuestions.objects.get(pk=pk)
        except PythonQuestions.DoesNotExist:
            question = None

        if question:
            serializer = GetRightAnswerSerializer(question)
            return Response(serializer.data, status=200)

        return Response()


class PythonTenQuestionsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # count of questions
        questions = random.sample(list(PythonQuestions.objects.all()), 10)
        serializer = PythonQuestionsSerializer(questions, many=True)
        return Response(serializer.data)
