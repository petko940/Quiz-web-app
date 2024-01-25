from django.urls import path

from apps.quiz.api.views import (SingleQuestionAPIView,
                                 PythonQuestionsAPIView,
                                 GetRightAnswerAPIView, SaveQuizResultAPIView, GetUsernameAPIView,
                                 )

from apps.quiz.views import (QuizView,
                             PythonQuiz, )

urlpatterns = [
    path('single-question/', QuizView.as_view(), name='single-question'),
    path('python-quiz/', PythonQuiz.as_view(), name='python-quiz'),

    # api
    path('api/<int:pk>/', SingleQuestionAPIView.as_view(), name='api-single-question'),
    path('api/questions-count/', PythonQuestionsAPIView.as_view(), name='api-question-count'),
    path('api/python-questions/', PythonQuestionsAPIView.as_view(), name='api-python-questions'),
    path('api/python-questions/<int:pk>/', GetRightAnswerAPIView.as_view(), name='api-get-right-answer'),
    path('api/save-quiz-result/', SaveQuizResultAPIView.as_view(), name='api-save-quiz-result'),
    path('api/get-username', GetUsernameAPIView.as_view(), name='api-get-username'),

]
