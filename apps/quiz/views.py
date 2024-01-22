import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.quiz.mixins import LogoutRequiredMixin
from apps.quiz.models import PythonQuestions


# Create your views here.
class QuizView(LogoutRequiredMixin, views.TemplateView):
    template_name = 'quiz/single-question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = random.choice(PythonQuestions.objects.all())
        return context


class PythonQuiz(LoginRequiredMixin, views.TemplateView):
    template_name = 'quiz/python-quiz.html'
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = random.sample(list(PythonQuestions.objects.all()), 10)
        context['index'] = 0
        return context
