from django.contrib import admin
from blog.models import Tag, Categories, Page


# Register your models here.
@admin.register(Tag)
class tagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
        "slug",
    )
    list_per_page = 10
    ordering = ("-id",)
    list_filter = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Categories)
class categoriesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
        "slug",
    )
    list_per_page = 10
    ordering = ("-id",)
    list_filter = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Page)
class pageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "is_published",
    )
    list_display_links = ("title",)
    search_fields = (
        "id",
        "title",
        "slug",
        "is_published",
    )
    list_per_page = 50
    ordering = ("-id",)
    list_filter = ("title", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_editable = ("is_published",)
