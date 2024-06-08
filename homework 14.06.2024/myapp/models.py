from django.db import models
from .validators import validate_phone_number, validate_email, validate_hashtag

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        validators=[validate_phone_number]
    )

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(
        max_length=100,
        validators=[validate_email]
    )

    def __str__(self):
        return f'{self.username} - {self.email}'

class Post(models.Model):
    content = models.TextField()
    hashtag = models.CharField(
        max_length=100,
        validators=[validate_hashtag]
    )

    def __str__(self):
        return f'{self.content} - {self.hashtag}'
