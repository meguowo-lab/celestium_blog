from django.contrib.auth.models import AbstractUser
from django.db.models import Model, ForeignKey, CharField, TextField, DateTimeField, CASCADE, ImageField


class User(AbstractUser):
    pass

class Post(Model):
    author = ForeignKey(to=User, on_delete=CASCADE)
    image = ImageField(upload_to="./static/images", blank=True, null=True)
    info = TextField()
    title = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)

class AbstractComment(Model):
    info = CharField(max_length=1000)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Comment(AbstractComment):
    author = CharField(max_length=30)
    post = ForeignKey(Post, on_delete=CASCADE, related_name='comments')

    class Meta:
        ordering = ['-created_at']
