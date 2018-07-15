from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Conversation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=128)
    user_in = models.TextField()
    braggi_out = models.TextField()
    intent = models.CharField(max_length=64)
    invoked_event = models.CharField(max_length=128)

    class Meta:
        ordering = ('created',)