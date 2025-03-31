from rest_framework import serializers
from backend.core.models import Genre


class GenreReadOnlySerializer(serializers.Serializer):
    public_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("public_id", "name", "description")
        read_only_fields = ("public_id",)
