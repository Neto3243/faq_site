from django.shortcuts import render
from .models import Question, Answer, Category, Comment
from user.models import Profile
from django.views import generic
from django.shortcuts import get_object_or_404


def index(request):
    num_quest = Question.objects.all().count()
    num_user = Profile.objects.all().count()
    num_answer = Answer.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_quest': num_quest,
            'num_user': num_user,
            'num_answer': num_answer
        }
    )


class QuestionListViews(generic.ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter()[:10]


def quest(request):
    que_st = Question.objects.all()
    cat_st = Category.objects.all()
    return render(
        request,
        'quest.html',
        context={
            'que_st': que_st,
            'cat_st': cat_st
        }
    )


class QuestionDetailViews(generic.DetailView):
    model = Question


def category(request, pk):
    cat_st = get_object_or_404(Category, pk=pk)
    que_st_1 = Question.objects.filter(category=pk)

    return render(
        request,
        'category.html',
        context={
            'cat_st': cat_st,
            'que_st_1': que_st_1
        }
    )