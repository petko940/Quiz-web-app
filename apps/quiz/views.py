import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic as views

from apps.quiz.mixins import LogoutRequiredMixin
from apps.quiz.models import PythonQuestions, QuizResult


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
        context['questions'] = PythonQuestions.objects.all()
        return context


class LeaderboardView(views.TemplateView):
    template_name = 'quiz/leaderboard.html'
    queryset = QuizResult.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['leaderboard_python'] = QuizResult.objects.all()
        sorted_by_correct_answers = self.queryset.filter(quiz_name='Python').order_by('-correct_answers', 'finish_time')

        page = self.request.GET.get('page', 1)
        paginator = Paginator(sorted_by_correct_answers, self.paginate_by)

        try:
            python_leaderboard = paginator.page(page)
        except PageNotAnInteger:
            python_leaderboard = paginator.page(1)
        except EmptyPage:
            python_leaderboard = paginator.page(paginator.num_pages)

        context['python_leaderboard'] = python_leaderboard
        return context
