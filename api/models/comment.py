from django.db import models

from .post import Post
from .user import User


class Comment(models.Model):
    content = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children')

    def __str__(self):
        return self.content
