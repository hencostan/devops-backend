from rest_framework import serializers
from backend.core.models import Author


class AuthorReadOnlySerializer(serializers.Serializer):
    public_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    biography = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    profile_picture = serializers.ImageField(read_only=True)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "public_id",
            "first_name",
            "last_name",
            "biography",
            "profile_picture",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("public_id", "created_at", "updated_at")
