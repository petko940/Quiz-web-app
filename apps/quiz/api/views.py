from rest_framework.views import APIView

from apps.quiz.models import PythonQuestions
from apps.quiz.api.serializers import SingleQuestionSerializer
from rest_framework.response import Response


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
