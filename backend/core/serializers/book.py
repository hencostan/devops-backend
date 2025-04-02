from rest_framework import serializers
from backend.core.models import Book
from backend.core.serializers.genre import GenreReadOnlySerializer
from backend.core.serializers.author import AuthorReadOnlySerializer


class BookReadOnlySerializer(serializers.Serializer):
    public_id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    edition = serializers.CharField(read_only=True)
    cover_image = serializers.ImageField(read_only=True)
    isbn = serializers.CharField(read_only=True)
    publisher = serializers.CharField(read_only=True)
    publication_date = serializers.DateField(read_only=True)
    authors = AuthorReadOnlySerializer(many=True, read_only=True)
    genres = GenreReadOnlySerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "public_id",
            "name",
            "description",
            "edition",
            "cover_image",
            "isbn",
            "publisher",
            "publication_date",
            "authors",
            "genres",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("public_id", "created_at", "updated_at")
