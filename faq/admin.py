from django.contrib import admin
from .models import Question, Answer, Comment, Category


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest_text', 'pub_date')
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest', 'answer_text', 'pub_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest' , 'comment_text', 'pub_date')


admin.site.register(Category)