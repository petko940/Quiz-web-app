from django.urls import path

from apps.quiz.api.views import (SingleQuestionAPIView,
                                 PythonTenQuestionsAPIView,
                                 GetRightAnswerAPIView, )

from apps.quiz.views import (QuizView,
                             PythonQuiz, )

urlpatterns = [
    path('single-question/', QuizView.as_view(), name='single-question'),
    path('python-quiz/', PythonQuiz.as_view(), name='python-quiz'),

    # api
    path('api/<int:pk>/', SingleQuestionAPIView.as_view(), name='api-single-question'),
    path('api/python-questions/', PythonTenQuestionsAPIView.as_view(), name='api-python-questions'),
    path('api/python-questions/<int:pk>/', GetRightAnswerAPIView.as_view(), name='api-get-right-answer'),
]
