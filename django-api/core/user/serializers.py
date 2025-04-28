from rest_framework import serializers

from core.user.models import User


class UserSerializer(serializers.ModelSerializer):
    # Rewriting some fields like the public id to be represented as the id of the object
    id = serializers.UUIDField(source="public_id", read_only=True, format="hex")

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "email",
            "is_active",
            "created",
            "updated",
        ]
        # List of all the fields that can only be read by the user
        read_only_fields = ["is_active", "created", "updated"]
