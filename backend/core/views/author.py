from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.core.models import Author
from backend.core.serializers.author import AuthorSerializer, AuthorReadOnlySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    lookup_url_kwarg = "public_id"
    lookup_value_regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    queryset = Author.objects.all()
    serializer_classes = {
        "list": AuthorReadOnlySerializer,
        "retrieve": AuthorReadOnlySerializer,
        "create": AuthorSerializer,
        "update": AuthorSerializer,
        "partial_update": AuthorSerializer,
    }
    serializer_default = AuthorSerializer

    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_default)
