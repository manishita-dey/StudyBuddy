from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True
    )  # One topic can have many rooms
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants=
    updated = models.DateTimeField(
        auto_now=True
    )  # will save everytime a change is made
    created = models.DateTimeField(
        auto_now_add=True
    )  # will save the first time the room is created

    class Meta:
        ordering = [
            "-updated",
            "-created",
        ]  # this will order the room list with updated first

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # if one room gets deleted, all children mesaages get deleted. One Room can have many messages
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]  # only first 50 characters will be shown
