from django.contrib.admin import site
from .models import User, Comment, Post

# Register your models here.

site.register(User)
site.register(Post)
site.register(Comment)
