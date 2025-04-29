from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.comment.models import Comment
from core.user.models import User
from core.user.serializers import UserSerializer
from core.post.models import Post
from core.post.serializers import PostSerializer


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(), slug_field="public_id"
    )

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")

        return value

    def validate_post(self, value):
        # The instance attribute holds the object that **will be modified** if there is a DELETE, PUT, or PATCH request. If this is a GET or POST request, this attribute is set to None.
        if self.instance:
            return self.instance.post

        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data

        post = Post.objects.get_object_by_public_id(rep["post"])
        rep["post"] = PostSerializer(post).data

        return rep

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True

        instance = super().update(instance, validated_data)

        return instance

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "body",
            "post",
            "edited",
            "created",
            "updated",
        ]
        read_only_fields = ["edited"]
