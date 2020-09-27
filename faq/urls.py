from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^quest/$', views.QuestionListViews.as_view(), name='quest'),
    re_path(r'^quests/$', views.quest, name='quests'),
    re_path(r'^quest/(?P<pk>\d+)$', views.QuestionDetailViews.as_view(), name='question-detail'),
    re_path(r'^category/(?P<pk>\d+)$', views.category, name='category'),
    re_path(r'^quest/new/$', views.quest_new, name='quest-new'),
    re_path(r'^comment/new/(?P<pk>\d+)$', views.comment_new, name='comment-new'),
    re_path(r'^answer/new/(?P<pk>\d+)$', views.answer_new, name='answer-new'),
]

