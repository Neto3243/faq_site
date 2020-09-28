from .models import Question, Comment, Answer, Category
from django import forms


class QuestForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quest_text']


class ComForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class AnsForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']