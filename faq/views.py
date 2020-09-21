from django.shortcuts import render
from .models import Question, Answer, Category, Comment
from user.models import Profile
from django.views import generic


def index(request):
    num_quest = Question.objects.all().count()
    num_user = Profile.objects.all().count()
    num_answer = Answer.objects.all().count()

    return render(
        request,
        'index.html',
        context = {
            'num_quest': num_quest,
            'num_user': num_user,
            'num_answer': num_answer
        }
    )