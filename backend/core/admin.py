from django.contrib import admin
from backend.core.models import Author, Book, Genre, User, Comment


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("public_id", "first_name", "last_name", "created_at", "updated_at")
    search_fields = ("first_name", "last_name")
    readonly_fields = ("public_id", "created_at", "updated_at")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("public_id", "name", "isbn", "publisher", "publication_date")
    search_fields = ("name", "isbn", "publisher")
    readonly_fields = ("public_id", "created_at", "updated_at")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("public_id", "name", "description")
    search_fields = ("name",)
    readonly_fields = ("public_id",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("public_id", "username", "email", "is_active", "is_staff")
    search_fields = ("username", "email")
    readonly_fields = ("public_id", "last_login", "date_joined")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("public_id", "user", "content_type", "object_id", "created_at")
    search_fields = ("content",)
    readonly_fields = ("public_id", "created_at", "updated_at")
