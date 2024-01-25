import random

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.quiz.models import PythonQuestions, QuizResult
from apps.quiz.api.serializers import SingleQuestionSerializer, PythonQuestionsSerializer, GetRightAnswerSerializer, \
    PythonQuizResultSerializer


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


# class ChooseTypeQuizAPIView(APIView):
#     result = None
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         self.result = data.get('result')
#         print(self.result)
#         return Response({'result': self.result.get('res')})


class PythonQuestionsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # count of questions
        # count = request.GET.get('count', 10)
        count = 1
        questions = random.sample(list(PythonQuestions.objects.all()), count)
        serializer = PythonQuestionsSerializer(questions, many=True)
        return Response(serializer.data)


class SaveQuizResultAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            correct_answers = int(request.data.get('correct_answers', 0))
            finish_time = int(request.data.get('finish_time', 0))
            quiz_name = request.data.get('quiz_name', '')
            quiz_name = quiz_name.split('-')[0].capitalize()

            result = QuizResult.objects.create(
                user=user,
                correct_answers=correct_answers,
                finish_time=finish_time,
                quiz_name=quiz_name,
            )

            serializer = PythonQuizResultSerializer(result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetUsernameAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'username': request.user.username})
