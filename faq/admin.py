from django.contrib import admin
from .models import Question, Answer, Comment, Category


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest', 'anr')
    list_filter = ('user', 'anr')
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest', 'ans')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment')


admin.site.register(Category)