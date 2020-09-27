from django.db import models
from user.models import Profile
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])


class Question(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    quest_text = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category)
    answer_bool = models.BooleanField(null=True)
    pub_date = models.DateField(null=True)

    class Meta:
        ordering = ["quest_text", "pub_date"]

    def __str__(self):
        return self.quest_text

    @property
    def test(self):
        if self.answer.answer_text is None:
            return False
        return True

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
    answer_text = models.TextField(max_length=1000)
    pub_date = models.DateField()

    class Meta:
        ordering = ["quest", "pub_date"]

    def __str__(self):
        return self.answer_text


class Comment(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    quest = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment_text = models.TextField(max_length=1000)
    pub_date = models.DateField()

    class Meta:
        ordering = ["quest", "-pub_date"]

    def __str__(self):
        return self.comment_text
