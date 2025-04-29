from django.db import models
from core.abstract.models import AbstractManager, AbstractModel


class CommentManager(AbstractManager):
    pass


class Comment(AbstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.PROTECT)
    post = models.ForeignKey(to="core_post.Post", on_delete=models.PROTECT)

    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return f"{self.author.name}"
