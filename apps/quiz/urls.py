from django.urls import path

from apps.quiz.api.views import (SingleQuestionAPIView,
                                 PythonQuestionsAPIView,
                                 GetRightPythonAnswerAPIView,
                                 SaveQuizResultAPIView,
                                 GetUsernameAPIView,
                                 JSQuestionsAPIView,
                                 GetRightJSAnswerAPIView,
                                 )

from apps.quiz.views import (QuizView,
                             PythonQuizView,
                             JSQuizView,
                             LeaderboardView,
                             RecentQuizView
                             )

urlpatterns = [
    path('single-question/', QuizView.as_view(), name='single-question'),
    path('python-quiz/', PythonQuizView.as_view(), name='python-quiz'),
    path('js-quiz', JSQuizView.as_view(), name='js-quiz'),

    # leaderboard
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),

    # recent-quizzes
    path('recent-quizzes/', RecentQuizView.as_view(), name='recent-quizzes'),

    # apis
    path('api/<int:pk>/', SingleQuestionAPIView.as_view(), name='api-single-question'),

    path('api/python-questions/', PythonQuestionsAPIView.as_view(), name='api-python-questions'),
    path('api/python-questions/<int:pk>/', GetRightPythonAnswerAPIView.as_view(), name='api-python-get-right-answer'),

    path('api/js-questions/', JSQuestionsAPIView.as_view(), name='api-js-questions'),
    path('api/js-questions/<int:pk>/', GetRightJSAnswerAPIView.as_view(), name='api-js-get-right-answer'),

    path('api/save-quiz-result/', SaveQuizResultAPIView.as_view(), name='api-save-quiz-result'),
    path('api/get-username', GetUsernameAPIView.as_view(), name='api-get-username'),

]
