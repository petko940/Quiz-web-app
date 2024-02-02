from django.db import models

from apps.users.models import CustomUser


# Create your models here.
class BaseQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    class Meta:
        abstract = True


class PythonQuestions(BaseQuestion):
    def __str__(self):
        return "Python"


class JSQuestions(BaseQuestion):
    def __str__(self):
        return "JavaScript"


class HTMLCSSQuestions(BaseQuestion):
    def __str__(self):
        return "HTML/CSS"


class QuizResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=50)
    correct_answers = models.IntegerField(default=0)
    finish_time = models.IntegerField()

    objects = models.Manager()
