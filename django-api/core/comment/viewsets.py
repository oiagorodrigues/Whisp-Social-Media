from django.http import Http404

from core.abstract.viewsets import AbstractViewSet
from core.comment.serializers import CommentSerializer
from core.comment.models import Comment
from core.auth.permissions import UserPermission


class CommentViewSet(AbstractViewSet):
    http_method_names = ("get", "post", "delete", "put")
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    # url: /api/posts/post_pk/comments/
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        post_pk = self.kwargs["post_pk"]
        if post_pk is None:
            return Http404

        return Comment.objects.filter(post__public_id=post_pk)

    # url: /api/posts/post_pk/comments/comment_pk/
    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs["pk"])

        self.check_object_permissions(self.request, obj)

        return obj
