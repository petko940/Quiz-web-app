# Generated by Django 5.0.1 on 2024-01-25 15:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_pythonquizresult_quiz_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PythonQuizResult',
            new_name='QuizResult',
        ),
    ]