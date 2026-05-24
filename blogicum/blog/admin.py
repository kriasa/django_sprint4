from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_published",
        "created_at",
    )
    list_editable = ("is_published",)
    search_fields = ("title", "description")
    list_filter = ("is_published", "created_at")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
        "created_at",
    )
    list_editable = ("is_published",)
    search_fields = ("name",)
    list_filter = ("is_published", "created_at")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "location",
        "pub_date",
        "is_published",
        "created_at",
    )
    list_editable = ("is_published", "category", "location")
    search_fields = ("title", "text")
    list_filter = (
        "is_published",
        "category",
        "location",
        "pub_date",
        "created_at",
    )
    date_hierarchy = "pub_date"
    raw_id_fields = ("author",)
