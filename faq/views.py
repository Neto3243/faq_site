from django.shortcuts import render
from .models import Question, Answer, Category, Comment
from user.models import Profile
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import QuestForm, ComForm, AnsForm
from django.shortcuts import redirect
from django.utils import timezone
from django.db import IntegrityError
from django.http import HttpResponse


def index(request):
    num_quest = Question.objects.all().count()
    num_user = Profile.objects.all().count()
    num_answer = Answer.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={
            'num_quest': num_quest,
            'num_user': num_user,
            'num_answer': num_answer,
            'num_visits': num_visits
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


def quest_new(request):
    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            quest_st = form.save(commit=False)
            quest_st.user = Profile.objects.get(user=request.user)
            quest_st.pub_date = timezone.now()
            quest_st.save()
            return redirect('question-detail', pk=quest_st.pk)
    else:
        form = QuestForm()
    return render(
        request,
        'faq/quest_new.html',
        {'form': form}
    )


def comment_new(request, pk):
    que_st = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        form = ComForm(request.POST)
        if form.is_valid():
            com_st = form.save(commit=False)
            com_st.user = Profile.objects.get(user=request.user)
            com_st.quest = Question.objects.get(id=que_st.pk)
            com_st.pub_date = timezone.now()
            com_st.save()
        return redirect('question-detail', pk=que_st.pk)
    else:
        form = ComForm()
    return render(
        request,
        'faq/comment_new.html',
        {'form': form}
    )


def answer_new(request, pk):
    que_st = get_object_or_404(Question, pk=pk)
    ans_st = Answer.objects.get(pk=que_st.pk)

    try:
        Answer.objects.get(pk=ans_st.pk)
        # group.users.add(User.objects.get(name='Julian'))
    except IntegrityError:
        return HttpResponse("<h1>ghbd</h1>")

    if request.method == "POST":
        form = AnsForm(request.POST)
        if form.is_valid():
            ans_st = form.save(commit=False)
            ans_st.user = Profile.objects.get(user=request.user)
            ans_st.quest = Question.objects.get(id=que_st.pk)
            ans_st.pub_date = timezone.now()
            ans_st.save()
        return redirect('question-detail', pk=que_st.pk)
    else:
        form = AnsForm()
    return render(
        request,
        'faq/answer_new.html',
        {'form': form}
    )