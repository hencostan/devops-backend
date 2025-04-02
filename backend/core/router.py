from rest_framework import routers

from backend.core import views

router = routers.DefaultRouter()
router.register(r"authors", views.AuthorViewSet, basename="authors")
router.register(r"books", views.BookViewSet, basename="books")
router.register(r"genres", views.GenreViewSet, basename="genres")
