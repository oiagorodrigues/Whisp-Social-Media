from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    # Rewriting some fields like the public id to be represented as the id of the object
    id = serializers.UUIDField(source="public_id", read_only=True, format="hex")
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
