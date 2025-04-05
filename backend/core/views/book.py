from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.core.models import Book
from backend.core.serializers.book import BookSerializer, BookReadOnlySerializer


class BookViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    lookup_url_kwarg = "public_id"
    lookup_value_regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    queryset = Book.objects.all()
    serializer_classes = {
        "list": BookReadOnlySerializer,
        "retrieve": BookReadOnlySerializer,
        "create": BookSerializer,
        "update": BookSerializer,
        "partial_update": BookSerializer,
    }
    serializer_default = BookSerializer

    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_default)
