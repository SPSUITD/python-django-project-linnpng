from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Channel(models.Model):
  name = models.CharField(max_length=50)


class Message(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)
