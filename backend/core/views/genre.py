from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.core.models import Genre
from backend.core.serializers.genre import GenreSerializer, GenreReadOnlySerializer


class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = "public_id"
    lookup_url_kwarg = "public_id"
    lookup_value_regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    queryset = Genre.objects.all()
    serializer_classes = {
        "list": GenreReadOnlySerializer,
        "retrieve": GenreReadOnlySerializer,
        "create": GenreSerializer,
        "update": GenreSerializer,
        "partial_update": GenreSerializer,
    }
    serializer_default = GenreSerializer

    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_default)
