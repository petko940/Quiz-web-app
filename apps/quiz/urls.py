from django.urls import path

from apps.quiz.api.views import SingleQuestionAPIView

from apps.quiz.views import (QuizView,
                             PythonQuiz
                             )

urlpatterns = [
    path('single-question/', QuizView.as_view(), name='single-question'),
    path('python-quiz/', PythonQuiz.as_view(), name='python-quiz'),

    # api
    path('api/<int:pk>/', SingleQuestionAPIView.as_view(), name='api-single-question'),
]
