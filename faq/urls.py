from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^quest/$', views.QuestionListViews.as_view(), name='quest'),
    re_path(r'^quests/$', views.quest, name='quests'),
]
