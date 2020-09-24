from django.db import models
from user.models import Profile
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    quest = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category)
    anr = models.BooleanField()

    class Meta:
        ordering = ["quest"]

    def __str__(self):
        return self.quest

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])


class Answer(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    quest = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
    )
    ans = models.TextField(max_length=1000)

    class Meta:
        ordering = ["quest"]

    def __str__(self):
        return self.ans


class Comment(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    quest = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    comment = models.TextField(max_length=1000)

    class Meta:
        ordering = ["quest"]
