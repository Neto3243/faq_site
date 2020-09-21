from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    STATUS = (
        ('Admin', 'Admin'),
        ('Moderator', 'Moderator'),
        ('User', 'User'),
    )
    status = models.CharField(max_length=10, choices=STATUS)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["status"]

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def created_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

